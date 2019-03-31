# Simple-Machine-Learning-Web-App

This web app allows users to send JSON data via HTTP requests.
Eg. curl -H "Content-Type: application/json" -X POST -d '{my_json_data}' http://localhost:5000/learn

The machine learning model can predict the target based on two features, one is a real value feature 'age', and the other one is a categorical feature 'species'. The target of this model is a real value target 'score'.
Eg. {'age' : 1.2, 'species' : 'dog', 'score' : 3.6}

The categorical features are encoded with OneHotEncoder to zeros and ones columns, and Bayesian Ridge Regression is chosen as the machine learning model to predict real value targets based on real value features.

This app will create a .csv file for the first time the server is started, and it will store every pieces of data in data.csv each time it receives a JSON data. 

Steps to run the python app:

Step 1. Start the server with command: nohup python3 -m ml_service &
Remarks: Run the app outside the ml_service folder

Step 2. Send training examples to http://localhost:5000/learn

Step 3. Train the model at http://localhost:5000/train

Step 4. Ask for a prediction at http://localhost:5000/predict

Step 5. Search for the PID of 'python3 -m ml_service' when you run command: ps -ef

Step 6. Kill the process with command: kill pid
