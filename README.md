# Simple-Machine-Learning-Web-App

This app will create a .csv file for the first time the server is started, and it will store every pieces of data in data.csv each time it receives a JSON data. 

Steps to run the python app
Step 1. Start the server with command: nohup python3 -m ml_service &

Step 2. Send training examples to http://localhost:5000/learn

Step 3. Train the model at http://localhost:5000/train

Step 4. Ask for a prediction at http://localhost:5000/predict

Step 5. Search for the PID of 'python3 -m ml_service' when you run command: ps -ef

Step 6. Kill the process with command: kill pid
