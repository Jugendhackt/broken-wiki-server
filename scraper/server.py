import wikipedia_histories
from flask import Flask

def count_edits_from_users(history):
    return_dict = {}
    for change in history:
        if change.user in return_dict.keys():
            return_dict[change.user] += 1
        else:
            return_dict.update({change.user: 1})
    return return_dict

alma_linux = wikipedia_histories.get_history('AlmaLinux')
print(count_edits_from_users(alma_linux))
app = Flask(__name__)


@app.route('/editcount')
def hello():
    return count_edits_from_users(alma_linux)
if __name__ == "__main__":
    app.run()