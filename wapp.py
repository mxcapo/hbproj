"""flask web app to communicate with browser"""
from flask import Flask, render_template, redirect, request, g, session as flasksesh
from flask import make_response
from newmod import session as dbsesh
from json import dumps
from dbcontrol import guests_by_party, one_party, guests_by_guest, filters
import filters


app = Flask(__name__)
app.secret_key = "aaslkjeegjkgdfkvjns"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/dash')
def dash():
    pass

@app.route('/base')
def base():
    pass

# @app.route('/view')
# def view():
#     g = make_response(dumps(filters()))
#     g.mimetype = "application/json"
#     return g

@app.route('/view/guests')
def view_guests_by_guest():
    view_guests = make_response(dumps(guests_by_guest()))
    view_guests.mimetype = "application/json"
    return view_guests

@app.route('/view/parties')
def parties():
    gparties = one_party()
    jsgparties = make_response(dumps(gparties))
    jsgparties.mimetype = "application/json"
    return jsgparties

if __name__ == '__main__':
    app.run(debug = True)
