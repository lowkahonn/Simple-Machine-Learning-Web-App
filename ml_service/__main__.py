#!/usr/bin/env python3

from flask import Flask, request
import csv
from pathlib import Path
import pandas as pd
from sklearn.linear_model import BayesianRidge
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# instantiate an Flask object
app = Flask(__name__)

# create a file called 'data.csv' if it doesn't exist
path = Path('data.csv')
if not path.is_file():
    with open('data.csv','w') as f:
        newfile = csv.writer(f)
        newfile.writerow(['age','species','score'])

# instantiate a regression model
reg = BayesianRidge()

@app.route('/learn', methods=['POST'])
def learn():
    # send examples to the server and store in 'data.csv'
    # structure the data
    if not request.is_json:
        return 'Please send JSON data\n'
    else:
        data = request.get_json()
        with open('data.csv','a') as f:
            writer = csv.writer(f)
            writer.writerow([data['age'],data['species'],data['score']])
        return 'ok\n'

@app.route('/train', methods=['POST'])
def train():
    # read data in 'data.csv'
    d = pd.read_csv('data.csv')
    # encode the categorical feature
    encoder = OneHotEncoder(sparse=False)
    species = np.array(d['species'])
    species = encoder.fit_transform(species.reshape(-1,1))
    species = species.tolist()
    # structure the data as list type
    age = d['age'].tolist()
    dt = []
    i = 0
    for a in age:
        dt.append([a])
        for s in species[i]:
            dt[i].append(s)
        i += 1
    # unzip dt and make them into lists
    # wrap it with list() to make a 2D list
    dt = list(map(list,zip(*dt)))
    # structure the data
    data = []
    j = 0
    for cols in dt:
        if j == 0:
            data = pd.Series(cols)
            j+=1
        else:
            data = pd.concat([data,pd.Series(cols)],axis=1)
    # fit into regression model
    target = d['score']
    reg.fit(data,target)
    return 'ok\n'

@app.route('/predict', methods=['POST'])
def predict():
    # get user's JSON input 
    if not request.is_json: 
        return 'Please send JSON data\n'
    else:
        user_input = request.get_json()
        # encode the categorical feature
        # in the same structure as how it has been trained
        d = pd.read_csv('data.csv')
        encoder = OneHotEncoder(sparse=False)
        species = d['species'].tolist()
        species.append(user_input['species'])
        species = np.array(species)
        species = encoder.fit_transform(species.reshape(-1,1))
        encoded_species = species[-1].tolist()
        # structure the query in shape
        query = [[user_input['age']]]
        for a in encoded_species:
            query[0].append(a)
        # predict and show the prediction
        pred = reg.predict(query)
        pred = pred.tolist()
        prediction = {"score": pred[0]}
        return f'{prediction}\n'

if __name__ == '__main__':
    app.run(debug=True)
 