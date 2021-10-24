import wikipedia_histories
from flask import Flask
from flask import request
from flask import jsonify
from lib import *

app = Flask(__name__)

@app.route('/editcount')
def editcount():
    question = request.args.get('q')
    results = wikipedia_histories.get_history(question, include_text=False)
    return jsonify(edit_count(results))

@app.route('/edittime')
def edittime():
    question = request.args.get('q')
    results = wikipedia_histories.get_history(questions, include_text=False)
    return jsonify(edit_time(results))

@app.route('/editmajor')
def editmajorcount():
    question = request.args.get('q')
    results = wikipedia_histories.get_history(questio, include_text=False)
    return jsonify(edit_time(results))

@app.route('/editminor')
def editminorcount():
    question = request.args.get('q')
    results = wikipedia_histories.get_history(questi, include_text=False)
    return jsonify(edit_time(results))

@app.after_request
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == "__main__":
    app.run()
    print("start")
