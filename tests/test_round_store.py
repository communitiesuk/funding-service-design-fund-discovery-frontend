import requests
from app.config import  ROUND_STORE_API_HOST, ROUND_ENDPOINT, ROUND_ID
from app.discovery.data import get_data


expected_data = get_data(f"{ROUND_STORE_API_HOST}/{ROUND_ENDPOINT}/{ROUND_ID}")

def test_round_store_data():
    """ 
    GIVEN our store api.
    WHEN a request made to the endpoint with requests module 
    to get the data from round-store with given {id}
    & then
    data checked against expected contents.
    """
    rounds = requests.get(f"{ROUND_STORE_API_HOST}/{ROUND_ENDPOINT}/{ROUND_ID}").json()
    assert rounds == expected_data
    

