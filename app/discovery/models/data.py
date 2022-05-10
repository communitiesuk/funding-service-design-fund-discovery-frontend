import json
import os
from typing import Tuple

import requests
from app.config import ACCOUNT_STORE_API_HOST
from app.config import FLASK_ROOT


def query_fund(query, endpoint: str):
    """Function return query from
    the fund store.

    Args:
        query: takes an query.
        endpoint (str): takes fund store endpoint.

    Returns:
        return query response from fund store.
    """
    if endpoint.startswith("https://"):
        if query:
            split_query = query.split()
            format_query = ",".join(split_query).replace(" ", "")
            response = requests.post(
                endpoint, params={"search_items": format_query}
            )
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return None
        else:
            response = requests.post(endpoint, params={"search_items": " "})
            if response.status_code == 200:
                data = response.json()
            else:
                return None
    else:
        data = get_local_fund(query, endpoint)
        return data

    return data


def get_local_fund(query, endpoint):
    """Function relates with query_local_fund
    function, return local funds data  &
    calls query_local_fund function.
    """
    api_data_json = os.path.join(
        FLASK_ROOT, "tests", "api_data", "local_endpoint_data.json"
    )
    json_data = open(api_data_json)
    api_data = json.load(json_data)
    json_data.close()
    if endpoint in api_data:
        return query_local_fund(query, endpoint, api_data)


def query_local_fund(queries, endpoint, data):
    """Function return query from
    the local fund store.

    Args:
        query: takes an query.
        endpoint (str): takes local fund store endpoint.

    Returns:
        return query response from local fund store.
    """
    fund_results = []
    for fund in data.get(endpoint):
        if queries:
            format_query = queries.split()
            for query in format_query:
                query_found = False
                if query in fund["fund_name"] or query in fund["fund_id"]:
                    fund_results.append(fund)
                    query_found = True
                if query_found:
                    break

        else:
            return data.get(endpoint)
    return fund_results


def convert_none_to_string(data):
    """Function return None data to
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


def get_fund_name(endpoint: str):
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
        data = get_local_fund_name(endpoint)
    return data


def get_local_fund_name(endpoint):
    """Function makes a get request data
    form fund store to retrieve the data

    Args:
        endpoint: Takes an fundstore endpoint

    Returns:
        Fund name to dispaly on the rounds page
    """

    api_data_json = os.path.join(
        FLASK_ROOT, "tests", "api_data", "local_endpoint_data.json"
    )
    json_data = open(api_data_json)
    api_data = json.load(json_data)
    json_data.close()
    endpoint_fund_id = endpoint.split("/")
    for data_values in api_data.values():
        for fund in data_values:
            for fund_id in endpoint_fund_id:
                if fund_id in fund.values():
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


def get_account(email_address: str = None, account_id: str = None):
    """get_account Using either an email address or account_id we
    grab the corresponding account from the account store.

    Args:
        email_address (str, optional): The account email address
        Defaults to None.
        account_id (str, optional): The account id. Defaults to None.

    Raises:
        TypeError: If both an email address or account id is given,
        a TypeError is raised.

    Returns:
        Tuple[int, Optional Response] Returns the status code
        and possible content in a tuple.
    """

    if email_address is None and account_id is None:

        raise TypeError("Requires an email address or account_id")

    req = requests.PreparedRequest()

    url = ACCOUNT_STORE_API_HOST + "/account"

    params = {"email_address": email_address, "account_id": account_id}

    req.prepare_url(url, params)

    response = requests.get(req.url)

    if response.status_code == 204:
        return 204, ""
    if response.status_code == 200:
        return 200, response.content
    else:
        return 400, ""


def post_account(email_address: str) -> Tuple[int, str]:
    """post_account An email address is used to
    (possibly) create a new account in the account
    store.

    Args:
        email_address (str): The email address we wish
        to create a new account with.

    Returns:
        Tuple[int, response data]: A tuple containing
        the status code and the  response data as a str
        - if successful.
    """

    req = requests.PreparedRequest()

    url = ACCOUNT_STORE_API_HOST + "/account"

    params = {"email_address": email_address}

    req.prepare_url(url, params)

    response = requests.post(req.url)

    if response.status_code == 409:
        return 409, ""
    if response.status_code == 200:
        return 200, response.content
