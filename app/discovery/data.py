
from urllib import response
from app.discovery.models import rounds
import requests
import os
import json
from flask import render_template
from app.config import FLASK_ROOT

def rounds_search(endpoint):
    """ 
    Given function is called in routes.py.
    Function requests the rounds data from round-store-datbase
    with given endpoint and run it through the model class 
    & renders to the template 
    """
    response = requests.get(endpoint)
    if response.status_code ==200:
        fund_rounds_data = response.json()
        fund_details = []
        if fund_rounds_data:
            for fund_rounds in fund_rounds_data:
                rounds_data = rounds.RoundStore(
                    fund_id=fund_rounds['fund_id'],
                    round_title=fund_rounds['round_title'],
                    round_id=fund_rounds['round_id'],
                    eligibility_criteria=fund_rounds['eligibility_criteria'],
                    opens= fund_rounds['opens'],
                    deadline= fund_rounds['deadline'],
                    application_url=fund_rounds['application_url']
                    )
                fund_details.append(rounds_data)
    else:
        message = "No rounds exist for this fund"
        return render_template("fund.html", 
                        message = message
                        )
    return render_template("fund.html",
                            fund_rounds_data = fund_rounds_data,
                            fund_details = fund_details,
                            rounds_data = rounds_data
                            )

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



def get_data(endpoint):
    if endpoint[:8] == 'https://':
        response = requests.get(endpoint)
        if response.status_code ==200:
            endpoint_data = response.json()
            return endpoint_data
        else:
            return None

    else:
        get_local_data("tests/api_data/local_endpoint_data.json")


# def get_local_data(endpoint):
#     with open(endpoint, 'r') as local_data:
#          local_data_read = local_data.read()
#          print("local data")
#          return local_data_read
         

       

def get_local_data(endpoint: str):
    api_data_json = os.path.join(
        FLASK_ROOT, "tests", "api_data",
         "local_endpoint_data.json"
    )
    fp = open(api_data_json)
    api_data = json.load(fp)
    fp.close()
    if endpoint in api_data:
        return api_data.get(endpoint)