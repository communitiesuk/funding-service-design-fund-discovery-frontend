from flask import Blueprint, render_template
from app.discovery.forms import SearchForm
from app.discovery.data import query_fund
from app.discovery.models.rounds import RoundStore
import requests
from app.config import (
    FUND_STORE_API_HOST, ROUND_STORE_API_HOST, FUND_ENDPOINT, ROUND_ENDPOINT
)

discovery_bp = Blueprint("discovery_bp", __name__,
  template_folder="templates")

"""
query is a global variable which is used 
in both routes to send the query to fund store database
"""
QUERY = []


@discovery_bp.route('/', methods=['GET', 'POST'])
def search_fund():
    """ 
    Given function creates a text field for search box &
    renders on index.html then 
    retrives input data from the user, run that data through 
    function query_fund from data.py to grab the fund 
    & renders back onto index.html 
    """
    form = SearchForm()
    if form.validate_on_submit():
        global QUERY
        QUERY = form.search.data.split(" ")
        fund_results = query_fund(
            QUERY, f"{FUND_STORE_API_HOST}/{FUND_ENDPOINT}")
        return render_template("search.html", query =QUERY, 
                              fund_results = fund_results,
                              form=form)
    else:
        render_template("404.html")                          
    return render_template("search.html", form=form)    


@discovery_bp.route('/round/<id>', methods=['GET', 'POST'])
def fund_rounds(id):
    fund_results = query_fund(
        QUERY, f"{FUND_STORE_API_HOST}/{FUND_ENDPOINT}")
    response  = requests.get(
        f"{ROUND_STORE_API_HOST}/{ROUND_ENDPOINT}/{id}")
    print(response.content)
    if response.status_code == 200:
        fund_rounds_data = response.json()
        fund_details = []
        if fund_rounds_data:
            for fund_rounds in fund_rounds_data:
                rounds_data = RoundStore(
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
                            fund_details = fund_details, 
                            fund_results = fund_results    
                        )

