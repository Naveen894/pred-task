import pandas as pd
from flask import Flask, request, jsonify, render_template, session,redirect,url_for,request
#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField
import pickle

app= Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():

    return render_template('index1.html')

def similar_products(task, n = 6):
        ms = model.similar_by_vector(task, topn= n+1)[1:]
        ms = [ms for t in ms for ms in t]
        return ms

#a=similar_products('Automatic Order CPE')
@app.route('/predict1')
def predict1():
    a=False
    task=request.args.get('task')

    a=similar_products(task)

    return render_template('predict1.html',a=a,task=task)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)
    #app.run(debug=True)
