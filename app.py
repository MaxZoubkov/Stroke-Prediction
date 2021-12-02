import flask
from flask import Flask, url_for, render_template
import pickle
import pandas as pd
import logging


app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        #app.logger.info(flask.request.form)    # useful to see what is submitted with the form
        
        input_list = flask.request.form
        # app.logger.info(X)
        # gender = flask.request.form['gender']
        # age = flask.request.form['age']
        # hypertension = flask.request.form['hypertension']
        # heart_disease = flask.request.form['heart_disease']
        # ever_married = flask.request.form['ever_married']
        # work_type = flask.request.form['work_type']
        # residence_type = flask.request.form['residence_type']
        # avg_glucose_level = flask.request.form['avg_glucose_level']
        # bmi = flask.request.form['bmi']
        # smoking_status = flask.request.form['smoking_status']

        # Feeding the model and outputting to the page will be here

        result = "some result"  # change to stroke prediction

        return render_template('main.html', input_list=input_list, result=result) # placeholder template


@app.route('/about')
def about():
    return render_template('result.html') #change to about.html


if __name__ == "__main__":
    app.run(debug=True)
        