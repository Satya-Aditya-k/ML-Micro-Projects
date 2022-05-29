from flask import Flask, render_template, request
import os.path
import pandas as pd
import pickle
loaded_model = pickle.load(open('model_pkl', 'rb'))

app=Flask(__name__)
app.secret_key = 'dfnvwjfiflynvksnfawknycl'


@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/prediction', methods=["POST"])
def predict():
    if request.method == 'POST':
        plength = request.form['plength']
        slength = request.form['slength']
        pwidth = request.form['pwidth']
        swidth = request.form['swidth']
        loaded_model = pickle.load(open('model_pkl', 'rb'))
        
        result = loaded_model.predict(pd.DataFrame([[slength,swidth,plength,pwidth]]))
        flower= []
        if result==0:
            flower='Iris-setosa'
        elif result==1:
            flower='Iris-virginica'
        elif result==2:
            flower='Iris-versicolor'
        
        
    return render_template('predict.html',flower = flower)
if __name__ == '__main__':
    app.run(debug=True)