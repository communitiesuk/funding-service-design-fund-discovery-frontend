"""
model.py contains classes & functions to be called
in for data processing & data alteration
"""

import requests
from datetime import datetime
from dataclasses import dataclass

@dataclass
class RoundStoreModel:
    """
    GIVEN class is a dataclass for round_store.
    DATA from round store funds runs through the model 
    for alteration.
    """
    fund_id: str
    round_title: str
    round_id: str
    eligibility_criteria :dict
    opens: datetime
    deadline: datetime    

    def format_opens(self, start):
        """
        GIVEN function is to alter the datetime string object 
        for self.opens for human readability.
        """      
        self.opens = datetime.strptime(start, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')
        return self.opens

    def format_deadline(self,end):
        """
        GIVEN function is to alter the datetime string object 
        for self.deadline for human readability.
        """     
        self.deadline = datetime.strptime(end, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')
        return self.deadline

  

def query_fund(keyword, endpoint):
    """
    GIVEN function is called to query the funds.
    WHEN a query searched by the user, this function runs 
    to retrive the query results from fund store
    """
    query_results = requests.post(endpoint, 
    params={'search_items':",".join(keyword)}).json()
    return query_results

