from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from firebase_admin import credentials, firestore, initialize_app
from flask_cors import CORS
import ml_utils

# init Flask app
app = Flask(__name__)
api = Api(app)
CORS(app)

# Init Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
users_ref = db.collection('users')
tasks_ref = db.collection('tasks')


class User(Resource):
    def get(self):
        return {"data": "Hello world"}
    def post(self):
        return


class Task(Resource):
    def get(self):
        return


#api.add_resource(User, "/user")
#api.add_resource(Task, "task")

@app.route('/predict', methods=['POST'])
def predict():
    tasks = request.json
    print(tasks)
    ml_utils.predictor(tasks)
    #print(ml_utils.predictor())
    #prediction = ml_utils.predictor()
    return jsonify({ 'result':  1 })

@app.route('/users', methods=['GET'])
def getUser():
    try:
        authHeader = request.headers['Authorization']
        username = authHeader.split(" ")[0]
        password = authHeader.split(" ")[1]
        print(username)
        print(password)

        foundUser = []
        foundTasks = []
        docs = users_ref.where(u'username', u'==', username).where(u'password', u'==', password).stream()

        for doc in docs:
            found = doc.to_dict()
            foundUser.append(found)

        if len(foundUser) != 1:
            raise Exception('Invalid username or password')

        tasks = tasks_ref.where(u'username', u'==', foundUser[0]['username']).stream()

        for t in tasks:
            found = t.to_dict()
            foundTasks.append(found)
        print(foundTasks)
        return jsonify(foundTasks)
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/users', methods=['POST'])
def addUser():
    try:
        print("foobar")
        content_type = request.headers.get('Content-Type')
        print(request.json['username'])
        print("here")
        users_ref.document(request.json['username']).set(request.json)

        return "success"
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/tasks', methods=['POST'])
def addTask():
    try:
        user = request.json['username']

        tasks_ref.add({ 'username': user,  })
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/tasks', methods=['DELETE'])
def deleteTask():
    try:
        taskId = request.json['taskId']

        tasks_ref.where(u'taskId', u'==', taskId).delete()
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/tasks', methods=['PUT'])
def updateTask():
    try:
        # add stress level
        return "" 
    except Exception as e:
        return f"An Error Occured: {e}"