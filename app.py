# import dependencies
from flask import (Flask, render_template, request)
import numpy as np
import pandas as pd
import joblib
from joblib import dump, load
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# import model and scaler
model = load('model/model.joblib')
X_scaler = load('model/model_scaler.joblib')

# import csv files
sel_state = pd.read_csv('data/derived/sel_state.csv')
sel_state = sel_state.set_index('state')
income_quartile = pd.read_csv('data/derived/income_quartile.csv')
income_quartile = income_quartile.set_index('state')

# function to process user input
def user_input(u_year, u_income, u_state, u_gender):
    user_df = pd.DataFrame()
    user_df['year'] = [u_year]
    u_state = u_state.lower()
    if int(u_income) <= income_quartile.loc[u_state, '_25']:
        user_df['quartile'] = [1]
    elif int(u_income) <= income_quartile.loc[u_state, '_50']:
        user_df['quartile'] = [2]
    elif int(u_income) <= income_quartile.loc[u_state, '_75']:
        user_df['quartile'] = [3]
    else:
        user_df['quartile'] = [4]
    user_df['state'] = u_state
    new_df = sel_state.loc[[u_state]]
    user_df = pd.merge(user_df, new_df, on = 'state')
    user_df = user_df.drop(columns=['state'])  
    u_gender = u_gender.lower()
    if u_gender == 'female':
        x = 1
        y = 0
    elif u_gender == 'male':  
        x = 0
        y = 1
    user_df['gender_Female'] = [x]
    user_df['gender_Male'] = [y] 
    return user_df

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/model')
def model2():
    return render_template('model.html')

@app.route('/model/data', methods=['POST'])
def model2data():
    year = request.form['html_year']
    income = request.form['html_income']
    gender = request.form['html_gender']
    state = request.form['html_state']
    data = user_input(year, income, state, gender)
    data_scaled = X_scaler.transform(data)
    life_expect = model.predict(data_scaled)
    return str(life_expect[0][0])

@app.route('/viz')
def viz():
    return render_template('viz.html')

if __name__ == "__main__":
    app.run(debug=True)