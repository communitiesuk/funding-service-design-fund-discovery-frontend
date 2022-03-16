from app.config import FUND_ENDPOINT
from app.config import FUND_SEARCH_ENDPOINT
from app.config import FUND_STORE_API_HOST
from app.config import ROUND_ENDPOINT
from app.config import ROUND_STORE_API_HOST
from app.discovery.data import get_data
from app.discovery.data import query_funds_data
from app.discovery.forms import SearchForm
from app.discovery.models.rounds import Rounds
from flask import Blueprint
from flask import render_template

discovery_bp = Blueprint("discovery_bp", __name__, template_folder="templates")


@discovery_bp.route("/", methods=["GET", "POST"])
def search_fund():
    """
    Given function creates a text field for search box &
    renders on index.html then
    retrives input data from the user, run that data through
    function query_fund from data.py to grab the fund
    & renders back onto index.html
    """
    form = SearchForm()
    if not form.validate_on_submit():
        return render_template("search.html", form=form)
    else:
        QUERY = form.search.data.split(" ")
        fund_results = query_funds_data(
            QUERY,
            f"{FUND_STORE_API_HOST}/{FUND_ENDPOINT}/{FUND_SEARCH_ENDPOINT}",
        )
        return render_template(
            "search.html", query=QUERY, fund_results=fund_results, form=form
        )


@discovery_bp.route("/round/<fund_id>", methods=["GET", "POST"])
def funds(fund_id):
    """
    GIVEN Function calls the RoundStore function
    from data model to check rounds with given endpoint
     & id.
     Function query_fund send QUERY to fund store
     so the fund name can be displayed onto the rounds page.
    """

    fund_rounds_data = get_data(
        f"{ROUND_STORE_API_HOST}/{ROUND_ENDPOINT}/{fund_id}"
    )
    fund_details = []
    if fund_rounds_data:
        for fund_round in fund_rounds_data:
            rounds_data = Rounds.fund_rounds(fund_round)
            fund_details.append(rounds_data)
    else:
        error = "No rounds exist for this fund"
        return render_template("fund.html", error=error)

    fund_json_response = get_data(
        f"{FUND_STORE_API_HOST}/{FUND_ENDPOINT}/{fund_id}"
    )

    return render_template(
        "fund.html",
        fund_details=fund_details,
        fund_json_response=fund_json_response,
    )
