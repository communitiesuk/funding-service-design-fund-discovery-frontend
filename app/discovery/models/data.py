import json
import os

import requests
from app.config import FLASK_ROOT


def get_funds(endpoint: str):
    """GIVEN function return funds
    from fund store endpoint
    """
    if "https://" in endpoint:
        response = requests.get(endpoint)
        if response.status_code == 200:
            data = response.json()
        else:
            return None
    else:
        data = get_local_funds(endpoint)

    return data


def get_local_funds(endpoint: str):
    """
    GIVEN function return funds from local
     api_data store during development
    """
    api_endpoint = os.path.join(
        FLASK_ROOT, "tests", "api_data", "local_endpoint_data.json"
    )
    with open(api_endpoint) as json_data:
        response = json.load(json_data)
        if endpoint in response:
            data = response.get(endpoint)
            return data


def query_funds(queries: str, funds: dict):
    """Summary:
    GIVEN function query funds
     from search homepage.

    Args:
        queries (str): Takes an query or
        multiple queries.
        funds (dict): Takes list of all funds.

    Returns:
        Returns expected query.
    """
    query_results = []

    for fund in funds:
        if queries:
            format_query = queries.split()
            print(f"FUNCTION - IF QUERY: {queries}")
            for query in format_query:
                if query in fund["fund_name"] or query in fund["fund_id"]:
                    query_results.append(fund)
        else:
            print("FUNCTION - ELSE")
            return funds

    return query_results


def convert_none_to_string(data):
    """GIVEN function return None data to
    empty string
    """
    if data is None:
        return ""
    return str(data)


def query_rounds(endpoint: str):
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
        data = query_local_rounds(endpoint)
    return data


def query_local_rounds(endpoint: str):
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


def get_local_data(endpoint):
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
