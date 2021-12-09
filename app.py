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

        with open('model/decision_tree_model.sav', 'rb') as f:
            model = pickle.load(f)
            app.logger.info(model)

        # feeding the model and outputting to the page

        # original features from dummies used
        dummies_list = ['gender', 'ever_married', 'work_type', 'Residence_type','smoking_status',]
        numerical_list = ['age', 'avg_glucose_level', 'bmi']
        feature_list = ['age','avg_glucose_level','gender_Male','bmi','ever_married_Yes','work_type_Private','work_type_Self-employed','Residence_type_Urban','smoking_status_never smoked','smoking_status_smokes']
        
        # create dummies from the input and remove original feature name
        for dummy in dummies_list:
            new_dummy = dummy + '_' + input_dict[dummy]
            input_dict[new_dummy] = 1
            input_dict.pop(dummy)

        # all input data is string, turn to int
        for numerical in numerical_list:
            input_dict[numerical] = float(input_dict[numerical])
        
        # if the feature does not exist in the input, then it's a dummy that is false
        input_list = []
        for feature in feature_list:
            if(feature in input_dict):
                input_list.append(input_dict[feature])
            else:
                input_list.append(0)
        
        app.logger.info(input_list)
        
        df = pd.DataFrame(data=[input_list], columns=[feature_list])
        app.logger.info(df)
        

        # prediction here
        prediction = model.predict(df)
        probability = model.predict_proba(df)
        app.logger.info(prediction)
        app.logger.info(probability)
        
        prediction = prediction[0]
        probability = probability[0,1]

        if prediction is 0:
          prediction = "High risk of stroke!"
        else:
          prediction = "Low risk of stroke."
        
        probability = "Probability of Stroke: " + str(probability*100) + "%"

        return render_template('main.html', result=prediction, probability=probability) # placeholder template


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
        