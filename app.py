import flask
from flask import Flask, url_for, render_template
import pickle
import pandas as pd
import re
import logging


app = Flask(__name__, template_folder='templates')




@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        app.logger.info(flask.request.form)    # useful to see what is submitted with the form
        
        input_dict = flask.request.form.to_dict()
        app.logger.info(input_dict)

        with open('model/model.sav', 'rb') as f:
            model = pickle.load(f)


        df = pd.DataFrame(input_dict, index=[0])
        app.logger.info(df)

        # Feeding the model and outputting to the page will be here
        # Assuming the model has a member element "model.feature_list"
        # input_list = []
        # for key, value in input_dict:
        #   input_list.append(key + '_' + value)
        # feature_list = model.feature_list
        # 
        # tuple = []
        # for feature in feature_list:
        #   if feature in input_list:
        #       tuple.append(1)
        #   else:
        #       tuple.append(0)
        # model_df = pd.DataFrame(columns=[feature_list])
        # for s in input_list:
        #   model_df[s] = 1




        # y_pred = model.predict(df)
        # probability = model.predict_proba(df)
        # result = y_pred[i]
        # if result is 0:
        #   result = "High risk of stroke!"
        # else:
        #   result = "Low risk of stroke."
        #probability = probability[0]

        result = "some result"  # change to stroke prediction
        probability = "some probability"    # change to stroke probability

        return render_template('main.html', result=result, probability=probability) # placeholder template


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
        