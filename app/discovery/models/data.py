import json
import os

import requests
from app.config import FLASK_ROOT
from app.discovery.models.local_data import get_test_funds_data
from app.discovery.models.local_data import get_test_rounds_data


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
        data = get_test_funds_data(keyword, endpoint)
    return data


def query_rounds_data(endpoint: str):
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
        data = get_test_rounds_data(endpoint)
    return data


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
        data = get_fund_name(endpoint)
    return data


def get_fund_name(endpoint):
    """Function makes a get request data
    form fund store to retrieve the data

    Args:
        endpoint: Takes an fundstore endpoint_

    Returns:
        Fund name to dispaly on the rounds page
    """

    api_data_json = os.path.join(
        FLASK_ROOT, "tests", "api_data", "local_endpoint_data.json"
    )
    json_data = open(api_data_json)
    api_data = json.load(json_data)
    json_data.close()
    endpoint_fund_id = endpoint.split("/")[2]
    for data_values in api_data.values():
        for fund in data_values:
            if endpoint_fund_id in fund.values():
                return fund


def list_data(json_data, data_func):
    """Function loops through json data &
    converts to list of dictionary

    Args:
        lst_data (dict): Takes json data
        data_func (class):

    Returns:
        list of dict data
    """
    listed_data = []
    for data in json_data:
        listed_data.append(data_func(data))
    return listed_data
