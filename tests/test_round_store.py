import requests
from app.discovery.models._endpoints import (ROUND_SEARCH_ENDPOINT,
                                             TEST_ROUND_SEARCH_ENDPOINT_RESPONSE)

# ERROR MESSAGE: requests.exceptions.TooManyRedirects: Exceeded 30 redirects.

# def test_round_search_endpoint_response():
#     """ 
#     GIVEN our round store api.
#     WHEN a request made to the round-store endpoint to check the status code
#     with no data in return.
#     """

#     response = requests.get(TEST_ROUND_SEARCH_ENDPOINT_RESPONSE)
#     assert response.status_code == 200


id = "funding-service-design"
def test_round_store_data():
    """ 
    GIVEN our store api.
    WHEN a request made to the endpoint with requests module 
    to get the data from round-store with given {id}
    & then
    data checked against expected contents.
    """
    expected_contents = [
        {'fund_id': 'funding-service-design',
        'round_title': 'Spring', 'round_id': 'spring', 
        'eligibility_criteria': {'max_project_cost': 1200000},
        'opens': '2022-02-01T00:00:01', 
        'deadline': '2022-06-01T00:00:00',
        'application_url': 'https://funding-service-design-form-runner.london.cloudapps.digital/funding-application'
        },
        {'fund_id': 'funding-service-design', 
        'round_title': 'Summer',
        'round_id': 'summer',
        'eligibility_criteria': {'max_project_cost': 1500000},
        'opens': '2022-06-01T00:00:01', 
        'deadline': '2022-08-31T00:00:00', 
        'application_url': 'https://funding-service-design-form-runner.london.cloudapps.digital/funding-application'
        },
        {'fund_id': 'funding-service-design',
        'round_title': 'Autumn',
        'round_id': 'autumn',
        'eligibility_criteria': {'max_project_cost': 10400000},
        'opens': '2022-09-01T00:00:01', 
        'deadline': '2022-11-30T00:00:00', 
        'application_url': 'https://funding-service-design-form-runner.london.cloudapps.digital/funding-application'
        }
        ]

    rounds = requests.get(f"{ROUND_SEARCH_ENDPOINT}/{id}").json()
    assert rounds == expected_contents
    