"""flask web app to communicate with browser"""
from flask import Flask, render_template, session
from flask import make_response
import model
import api
from json import dumps


app = Flask(__name__)
app.secret_key = "aaslkjeegjkgdfkvjns"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/view/parties')
def parties():
    jsgparties = make_response(dumps(api.one_party()))
    jsgparties.mimetype = "application/json"
    return jsgparties


def blank_view():
    jsga = [tup[0] for tup in api.grouping_headers()]
    jsg = make_response(dumps(jsga))
    jsg.mimetype = "application/json"
    # print dumps(jsga)
    gr = make_response(dumps(api.groups_side_filters()))
    print gr
    return make_response(dumps(api.groups_side_filters()))

@app.route('/view')
def trying():
    return blank_view()
    
@app.route('/filtertest')
def filter_test():
    return render_template('filtertest.html')

@app.route('/guest_card.html')
def guest_card():
    return render_template('guest_card.html')

if __name__ == '__main__':
    app.run(debug = True)
