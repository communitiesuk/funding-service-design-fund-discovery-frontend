import requests
from app.discovery.models.rounds import RoundStore

def query_fund(keyword, endpoint):
    """
    GIVEN function is called to query the funds.
    WHEN a query searched by the user, this function runs 
    to retrive the query results from fund store
    """
    response = requests.post(endpoint, 
    params={'search_items':",".join(keyword)})
    if response.status_code == 200:
        query_results = response.json()
        return query_results


def query_fund_rounds(fund_rounds):
    """
    GIVEN function is a data class from app/models/rounds.py
     & is called in app/discovery/routes fund_rounds
      to retrive the data from round store
    """
    store_rounds_data = RoundStore(
                    fund_id=fund_rounds['fund_id'],
                    round_title=fund_rounds['round_title'],
                    round_id=fund_rounds['round_id'],
                    eligibility_criteria=fund_rounds['eligibility_criteria'],
                    opens= fund_rounds['opens'],
                    deadline= fund_rounds['deadline'],
                    application_url=fund_rounds['application_url']
                    )
    return store_rounds_data
    