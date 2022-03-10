from app.discovery.data import query_fund
from app.config import FUND_STORE_API_HOST, FUND_ENDPOINT

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

def test_funds_store_data():
    """
     GIVEN our fund store api. 
    WHEN a request made to the fund-store endpoint with query_fund() function 
    to get the data with query keyword "fund" that is expected to grab all
    funds & then 
    funds checked against expected contents.
    """

    funds = query_fund("fund", f"{FUND_STORE_API_HOST}/{FUND_ENDPOINT}")
    assert funds == expected_contents
    


