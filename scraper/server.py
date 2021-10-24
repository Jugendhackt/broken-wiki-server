import wikipedia_histories
from flask import Flask
from flask import request
from flask import jsonify
#from flask import render_template
from lib import *

app = Flask(__name__)

#@app.route("/")
#def index():
#    return render_template("index.html") 

#@app.route("/credits")
#def credits():
#    return render_template("credits.html") 

@app.route('/editcount')
def editcount():
    question = request.args.get('q')
    results = wikipedia_histories.get_history(question, include_text=False)
    return jsonify(edit_count(results))

@app.route('/edittime')
def edittime():
    questions = request.args.get('q')
    #if not search:
    #    search = "AlmaLinux"
    results = wikipedia_histories.get_history(questions, include_text=False)
    return jsonify(edit_time(results))

@app.after_request
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == "__main__":
    app.run()
    print("start")
