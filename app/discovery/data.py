
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
    fund_rounds_data = requests.get(endpoint).json()
    fund_details = []
    if fund_rounds_data:
        for f in fund_rounds_data:
            rounds_data = model.RoundStoreModel(
                fund_id=f['fund_id'],
                round_title=f['round_title'],
                round_id=f['round_id'],
                eligibility_criteria=f['eligibility_criteria'],
                opens= f['opens'],
                deadline= f['deadline']
                )
            # -format the datetime string for opens & deadline
            rounds_data.format_opens(rounds_data.opens)
            rounds_data.format_deadline(rounds_data.deadline)


            fund_details.append(rounds_data)
    else:
        message = "No rounds available"
        return render_template("fund.html", 
                        message = message
                        )

    return render_template("fund.html", 
                            fund_rounds_data = fund_rounds_data,
                            fund_details = fund_details,
                            rounds_data = rounds_data
                            )
                            
            

