
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
    #return jsonify(request.form)

    # product_name = request.form["product_name"]
    # flash(f"Product '{product_name}' created successfully!", "success") # use the "success" category to correspond with twitter bootstrap alert colors
    return render_template("eventresults.html", state_name=state_name)
