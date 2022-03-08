
from app.discovery.models import model
import requests
from flask import render_template

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
                print(fund_rounds)
                rounds_data = model.RoundStoreModel(
                    fund_id=fund_rounds['fund_id'],
                    round_title=fund_rounds['round_title'],
                    round_id=fund_rounds['round_id'],
                    eligibility_criteria=fund_rounds['eligibility_criteria'],
                    opens= fund_rounds['opens'],
                    deadline= fund_rounds['deadline'],
                    application_url=fund_rounds['application_url']
                    )
        
                # -format the datetime string for opens & deadline
                rounds_data.format_opens(rounds_data.opens)
                rounds_data.format_deadline(rounds_data.deadline)
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
                            
            

