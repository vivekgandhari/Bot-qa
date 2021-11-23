import os
from flask import Flask,requests

app = Flask(__name__)

@app.route("/")
def start():
    querry = requests.args['name']
    return "Working "+querry



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
