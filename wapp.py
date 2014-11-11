"""flask web app to communicate with browser"""
from flask import Flask, render_template, redirect, request, g, session as flasksesh
from flask import make_response
import newmod
from newmod import session as dbsesh
from json import dumps
from dbcontrol import guests_by_party, one_party, guests_by_guest


app = Flask(__name__)
app.secret_key = "aaslkjeegjkgdfkvjns"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/dash')
def dash():
    return render_template("dash.html")

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/view')
def view():
    pass

@app.route('/view/party')
def view_guests_by_party():
    view_parties = guests_by_party()
    view_parties_js = make_response(dumps(view_parties))
    view_parties_js.mimetype = "application/json"
    # render_template('viewparties.html')
    return view_parties_js

@app.route('/view/guests')
def view_guests_by_guest():
    view_guests = make_response(dumps(guests_by_guest()))
    view_guests.mimetype = "application/json"
    return view_guests

@app.route('/parties')
def parties():
    gparties = one_party()
    jsgparties = make_response(dumps(gparties))
    jsgparties.mimetype = "application/json"
    return jsgparties

@app.route('/angular')
def angular():
    return render_template("partycard.html")

if __name__ == '__main__':
    app.run(debug = True)
