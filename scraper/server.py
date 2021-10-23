import wikipedia_histories
from flask import Flask
from flask import request
from flask import jsonify
from lib import *

#print(count_edits_from_users(alma_linux))
app = Flask(__name__)


@app.route('/editcount')
def editcount():
    search = request.args.get('search')
    results = wikipedia_histories.get_history(search)
    return jsonify(count_edits_from_users(results))
if __name__ == "__main__":
    app.run()
