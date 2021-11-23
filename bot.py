import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
#     querry = input("Please input your question: ")
    print("The code is yet to be updated to answer your question: "+"\n"+"Thank you")
    return "Working"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
