import wikipedia_histories
from flask import Flask
from lib import *

alma_linux = wikipedia_histories.get_history('AlmaLinux')
print(count_edits_from_users(alma_linux))
app = Flask(__name__)


@app.route('/editcount')
def hello():
    return count_edits_from_users(alma_linux)
if __name__ == "__main__":
    app.run()
