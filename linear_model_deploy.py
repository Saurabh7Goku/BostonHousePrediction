from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np

# Create Flask App
app = Flask(__name__)
#Model =  joblib.load('model2.pkl')
#col_names = joblib.load('col.pkl')

# Create API routing call
@app.route('/')
def home():
    return render_template("index.html")


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, -1)
    loaded_model = joblib.load('model3.pkl')
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = round(float(ValuePredictor(to_predict_list)), 2)
        return render_template("index.html", prediction_text=f'The Price Prediction : ${(result*1000)-3129}')

if __name__ == '__main__':
    app.run(debug=True)