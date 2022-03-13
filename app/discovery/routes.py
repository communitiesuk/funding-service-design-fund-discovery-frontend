from flask import Blueprint, render_template
import os
from app.discovery.forms import SearchForm
from app.discovery.data import query_fund
from app.discovery.data import rounds_search
from app.config import (
    FUND_STORE_API_HOST, ROUND_STORE_API_HOST, FUND_ENDPOINT, ROUND_ENDPOINT
)

from json import JSONEncoder
discovery_bp = Blueprint("discovery_bp", __name__,  template_folder="templates")

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
        query = form.search.data.split(" ")
        fund_results = query_fund(query, f"{FUND_STORE_API_HOST}/{FUND_ENDPOINT}")
        return render_template("search.html", query =query, 
                              fund_results = fund_results,
                              form=form)
    else:
        render_template("404.html")                          
    return render_template("search.html", form=form)    
 

@discovery_bp.route('/round/<id>', methods=['GET', 'POST'])
def fund_rounds(id):
    """
    Function calls the function from data model to 
    check rounds with given endpoint & id. 
    """
    rounds = rounds_search(f"{ROUND_STORE_API_HOST}/{ROUND_ENDPOINT}/{id}")
    return rounds
