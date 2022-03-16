import json
import os

import requests
from app.config import FLASK_ROOT


def query_funds_data(keyword: str, endpoint: str):
    """Function takes post request to
    query data from fund store
    Args:
        keyword (str): takes user input
        endpoint (str): takes api_host & endpoint
    Returns: list of json data

    """
    if endpoint[:8] == "https://":
        response = requests.post(
            endpoint, params={"search_items": ",".join(keyword)}
        )
        if response.status_code == 200:
            data = response.json()
        else:
            return None
    else:
        data = get_local_data(endpoint)
    return data


def get_local_data(endpoint: str):
    api_data_json = os.path.join(
        FLASK_ROOT, "tests", "api_data", "local_endpoint_data.json"
    )
    json_data = open(api_data_json)
    api_data = json.load(json_data)
    json_data.close()
    print(api_data)
    if endpoint in api_data:
        return api_data.get(endpoint)


def get_data(endpoint: str):
    """Function takes get request to
    get data from fund store
    Args:
        endpoint (str): api_endpoint
    Returns:
        list of json data
    """
    if endpoint[:8] == "https://":
        response = requests.get(endpoint)
        if response.status_code == 200:
            data = response.json()
        else:
            return None
    else:
        data = get_local_data(endpoint)
    return data
