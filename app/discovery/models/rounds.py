"""
model.py contains classes & functions to be called
in for data processing & data alteration
"""
from datetime import datetime
from dataclasses import dataclass

@dataclass
class RoundStore:
    """
    GIVEN class is a dataclass to manage Rounds
    """
    fund_id: str
    round_title: str
    round_id: str
    eligibility_criteria :dict
    opens: datetime
    deadline: datetime    
    application_url: str

    @property
    def opens_formatted(self):
        """
        GIVEN function is to alter the datetime string object 
        for self.opens for human readability.
        """      
        return datetime.strptime(self.opens, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')
    
    @property
    def deadline_formatted(self):
        """
        GIVEN function is to alter the datetime string object 
        for self.deadline for human readability.
        """     
        return datetime.strptime(self.deadline, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')

