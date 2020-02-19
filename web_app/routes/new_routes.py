import ticketpy
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("API_KEY")

from flask import Blueprint, request, render_template, jsonify, flash, redirect #, url_for

new_routes = Blueprint("new_routes", __name__)

@new_routes.route('/eventform')
def eventform():
    print("VISITING THE EVENT FORM PAGE")
    return render_template("eventform.html")

@new_routes.route('/getevents', methods=["POST"])
def getevents():
    print("Get Events")
    print("FORM DATA:", dict(request.form))
    state_name = request.form["state"]


    tm_client = ticketpy.ApiClient(API_KEY)
    pages = tm_client.events.find(
        classification_name='Hip-Hop',
        state_code=state_name,
        #state_code=location_input,
        start_date_time='2020-01-01T01:00:00Z',
        end_date_time='2020-03-02T01:00:00Z'
        #start_date_time='2020-',month_input,'-',day_input,'T01:00:00Z',
        #end_date_time='2020-',month_input,'-',day_input,'T24:00:00Z'
    ).limit(10)
    for event in pages:
        print(event)
        print(type(event))

    #return jsonify(request.form)

    # product_name = request.form["product_name"]
    # flash(f"Product '{product_name}' created successfully!", "success") # use the "success" category to correspond with twitter bootstrap alert colors
    return render_template("eventresults.html", state_name=state_name, events=pages)
