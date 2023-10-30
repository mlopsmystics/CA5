import os
from flask import Flask, request, jsonify, render_template
from todo import Todo as _Todo

import mysql.connector

app = Flask(__name__)

Todo = None


import time
import mysql.connector

# Define the function to establish a connection to the database with retry logic
def connect_to_db_with_retry():
    max_retries = 5
    retry_count = 0
    while retry_count < max_retries:
        try:
            if os.environ.get('ENV') is None:
                os.environ['ENV'] = 'local'
            if os.environ.get('ENV') == 'container':
                dbHost = os.environ.get('DB_HOST')
            if os.environ.get('ENV') == 'local':
                dbHost = 'localhost'

            db = mysql.connector.connect(
                host=dbHost,
                port=3306,
                user="root",
                password="root",
                database="TODO"
            )
            return db
        except mysql.connector.Error as err:
            print(f"Failed to connect to the database. Retry attempt {retry_count + 1}/{max_retries}")
            retry_count += 1
            time.sleep(5)  # Wait for 5 seconds before retrying
    # If the connection still cannot be established after retries, handle the error appropriately
    raise Exception("Failed to connect to the database after multiple retries.")

# Call the function to establish a connection to the database
db = connect_to_db_with_retry()

Todo = _Todo(db)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addTask', methods=['POST'])
def addTask():
    data = request.get_json()
    name = data['name']
    description = data['description']
    dueDate = data['dueDate']
    task = Todo.addTask(name, description, dueDate)
    return jsonify({'task': task.__dict__})

@app.route('/getTasks', methods=['GET'])
def getTasks():
    tasks = Todo.getTasks()
    return jsonify({'tasks': [task.__dict__ for task in tasks]})

@app.route('/deleteTask/<id>', methods=['DELETE'])
def deleteTask(id):
    result = Todo.deleteTask(id)
    return jsonify({'result': result})

@app.route('/updateTask/<id>', methods=['PUT'])
def updateTask(id):
    data = request.get_json()
    name = data['name']
    description = data['description']
    status = data['status']
    dueDate = data['dueDate']
    task = Todo.updateTask(id, name, description, status, dueDate)
    if not task:
        return jsonify({'task': None})

    return jsonify({'task': task.__dict__})

@app.route('/searchTask/<name>', methods=['GET'])
def searchTask(name):
    if name == '':
        tasks = Todo.getTasks()
    else:
        tasks = Todo.searchTask(name)
    return jsonify({'tasks': [task.__dict__ for task in tasks]})

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True, port=5000)

    # Close the cursor and the database connection when done
    Todo.db.cursor.close()
    Todo.db.close()