import json
import os

from app.config import FLASK_ROOT

TEST_FUND_STORE_API_HOST = "fund_store"


def get_test_funds_data(keyword: list, endpoint: str):
    """Function grabs the data from local
    database and covert funds data into json
    Args:
        endpoint (str): takes the api endpoint

    Returns:
        return local data form tests/api_data in json format
    """
    api_data_json = os.path.join(
        FLASK_ROOT, "tests", "api_data", "local_endpoint_data.json"
    )
    json_data = open(api_data_json)
    api_data = json.load(json_data)
    json_data.close()
    if endpoint in api_data:
        fund_results = []
        for data in api_data.get(endpoint):
            query = ",".join(keyword)
            if query in data["fund_id"] or query in data["fund_name"]:
                fund_results.append(data)
        return fund_results


def get_test_rounds_data(endpoint: str):
    """Function grabs the data from local
    database and covert rounds data into json
    Args:
        endpoint (str): takes the api endpoint

    Returns:
        return local data form tests/api_data in json format
    """
    api_data_json = os.path.join(
        FLASK_ROOT, "tests", "api_data", "local_endpoint_data.json"
    )
    json_data = open(api_data_json)
    api_data = json.load(json_data)
    json_data.close()
    if endpoint in api_data.keys():
        rounds = []
        for data in api_data.get(endpoint):
            rounds.append(data)
        return rounds
