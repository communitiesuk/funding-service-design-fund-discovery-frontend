from app.config import AUTHENTICATOR_MAGIC_LINK_URL
from app.config import FUND_STORE_API_HOST
from app.config import FUNDS_SEARCH_URL
from app.config import FUNDS_URL
from app.config import ROUND_STORE_API_HOST
from app.config import ROUNDS_URL
from app.discovery.forms import SearchForm
from app.discovery.models.data import get_fund_name
from app.discovery.models.data import list_data
from app.discovery.models.data import query_fund
from app.discovery.models.data import query_rounds
from app.discovery.models.rounds import Rounds
from flask import Blueprint
from flask import render_template
from flask import request

discovery_bp = Blueprint("discovery_bp", __name__, template_folder="templates")


@discovery_bp.route("/")
def search_funds():
    """GIVEN route takes a search form, retrieves
    user input/query & return query response
    from fund store.
    """
    form = SearchForm()
    query = request.args.get("search", "")

    query_response = query_fund(
        query, FUNDS_SEARCH_URL.format(host=FUND_STORE_API_HOST)
    )
    return render_template(
        "search.html",
        query=query,
        query_response=query_response,
        form=form,
    )


@discovery_bp.route("/round/<fund_id>", methods=["GET", "POST"])
def fund_rounds(fund_id):
    """
    GIVEN Function calls the RoundStore function
    from data model to check rounds with given endpoint
     & id.
     Function query_fund send QUERY to fund store
     so the fund name can be displayed onto the rounds page.
    """
    fund_rounds_data = query_rounds(
        ROUNDS_URL.format(host=FUND_STORE_API_HOST, fund_id=fund_id)
    )

    if fund_rounds_data:
        rounds = list_data(fund_rounds_data, Rounds.fund_rounds)
    else:
        error = "No rounds exist for this fund"
        return render_template("fund.html", error=error)

    fund = get_fund_name(
        FUNDS_URL.format(host=FUND_STORE_API_HOST, fund_id=fund_id)
    )

    return render_template(
        "fund.html",
        fund=fund,
        rounds=rounds,
        authenticator_magic_link_url=AUTHENTICATOR_MAGIC_LINK_URL,
    )
