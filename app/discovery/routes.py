from flask import Blueprint, render_template
from app.discovery.forms import SearchForm
from app.discovery.data import query_fund
from app.discovery.models._endpoints import FUND_SEARCH_ENDPOINT, ROUND_SEARCH_ENDPOINT
from app.discovery.data import rounds_search

discovery_bp = Blueprint("discovery_bp", __name__,  template_folder="templates")

@discovery_bp.route('/', methods=['GET', 'POST'])
def search_fund():
    """ 
    Given function creates a text field for search box &
    renders on index.html then 
    retrives input data from the user, run that data through 
    function query_fund from models to grab the fund 
    & renders back onto index.html 
    """
    form = SearchForm()
    if form.validate_on_submit():
        query = form.search.data.split(" ")
        fund_results = query_fund(query, FUND_SEARCH_ENDPOINT)
        return render_template("search.html", query =query, 
                              fund_results = fund_results,
                              form=form)
    return render_template("search.html", form=form)    


@discovery_bp.route('/round/<id>', methods=['GET', 'POST'])
def fund_rounds(id):
    """
    Function calls the function from data model to 
    check rounds with given endpoint & id. 
    """
    rounds = rounds_search(f"{ROUND_SEARCH_ENDPOINT}/{id}")
    return rounds



