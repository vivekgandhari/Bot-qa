import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
    querry = ""
    while(querry!="exit"):
        querry = input("Please input your question: ")
        print("The code is yet to be updated to answer your question: "+querry"+"\n"+"Thank you")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
