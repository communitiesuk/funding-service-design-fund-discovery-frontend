import requests


def query_fund(keyword, endpoint):
    """
    GIVEN function is called to query the funds.
    WHEN a query searched by the user, this function runs
    to retrive the query results from fund store
    """
    response = requests.post(
        endpoint, params={"search_items": ",".join(keyword)}
    )
    if response.status_code == 200:
        query_results = response.json()
        return query_results


def request_json_fund(api_endpoints):

    response = requests.get(api_endpoints)

    if response.status_code == 200:
        return response.json()


def json_funds():
    pass
