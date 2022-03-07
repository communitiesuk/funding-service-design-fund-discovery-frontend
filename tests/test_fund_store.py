import requests
from app.discovery.models.model import query_fund
from app.discovery.models._endpoints import (FUND_SEARCH_ENDPOINT, 
                                             TEST_FUND_SEARCH_ENDPOINT_RESPONSE)

def test_funds_store_endpoint_response():
    """ 
    GIVEN our fund store api. 
    WHEN a request made to the fund-store endpoint to check the status code
    with no data in return.
    """
    response = requests.get(TEST_FUND_SEARCH_ENDPOINT_RESPONSE)
    assert response.status_code == 200


def test_funds_store_data():
    """
     GIVEN our fund store api. 
    WHEN a request made to the fund-store endpoint with query_fund() function 
    to get the data with query keyword "fund" that is expected to grab all
    funds & then 
    funds checked against expected contents.
    """

    expected_contents = [
        {'fund_name': "Harry's breakfast fund", 
        'fund_id': 'harry-s-breakfast-fund',
         'fund_description': "A fund designed to supply Harry's endless supply of muesli."
         }, 
         {'fund_name': "Ram's Get Fit Feb fund",
          'fund_id': 'ram-s-get-fit-feb-fund', 
          'fund_description': 'A fund designed to supply gym memberships to home workers during Feb.'
          }, 
          {'fund_name': 'Funding service design', 
          'fund_id': 'funding-service-design',
           'fund_description': 'A fund designed to test the funding service design dev team.'
           }
           ]

    funds = query_fund("fund", FUND_SEARCH_ENDPOINT)
    assert funds == expected_contents
    


