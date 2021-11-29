# import os
# from flask import Flask,requests

# app = Flask(__name__)

# @app.route('/form')
# def form():
#     return render_template('form.html')
 
# @app.route('/data/', methods = ['POST', 'GET'])
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#         return render_template('data.html',form_data = form_data)
 
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)
from pywebio.input import input
from pywebio.output import put_text

def bmi():
    height = input("Your height:")
    weight = input("Your weight:")
    
    BMI_cal = height/weight
    
    put_text(BMI_cal)


if __name__ == '__main__':
    pywebio.start_server(bmi,port=80)
