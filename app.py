import flask
from flask import Flask
import pickle
import pandas as pd


app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))

    elif flask.request.method == 'POST':
        gender = flask.request.form['gender']
        age = flask.request.form['age']
        hypertension = flask.request.form['hypertension']
        heart_disease = flask.request.form['heart_disease']
        ever_married = flask.request.form['ever_married']
        work_type = flask.request.form['work_type']
        residence_type = flask.request.form['residence_type']
        avg_glucose_level = flask.request.form['avg_glucose_level']
        bmi = flask.request.form['bmi']
        smoking_status = flask.request.form['smoking_status']


if __name__ == "__main__":
    app.run(debug=True)
        