"""flask web app to communicate with browser"""
from flask import Flask, render_template, redirect, request, g, session as flasksesh
from flask import make_response
from newmod import session as dbsesh
from json import dumps
from dbcontrol import guests_by_party, one_party, guests_by_guest, grouping_headers
from dbcontrol import groups_side_filters

app = Flask(__name__)
app.secret_key = "aaslkjeegjkgdfkvjns"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/view/parties')
def parties():
    gparties = one_party()
    jsgparties = make_response(dumps(gparties))
    jsgparties.mimetype = "application/json"
    return jsgparties

@app.route('/groupings')
def blank_view():
    jsga = [tup[0] for tup in grouping_headers()]
    jsg = make_response(dumps(jsga))
    jsg.mimetype = "application/json"
    # print dumps(jsga)
    gr = make_response(dumps(groups_side_filters()))
    print gr
    return make_response(dumps(groups_side_filters()))

@app.route('/filtertest')
def filter_test():
    return render_template('filtertest.html')

if __name__ == '__main__':
    app.run(debug = True)
