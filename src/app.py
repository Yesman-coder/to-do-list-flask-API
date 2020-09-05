# Command to run the project on a local server: pipenv run python src/app.py

 flask import Flask, request
from flask import jsonify, json

app = Flask(__name__)

todos = [
        {"label": "My first Task", "done": False},
        {"label": "Sample Task 2", "done": False}
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
    request_body = jsonify(todos)
    return request_body

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    print("Incoming request with the following body" , request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position -1)
    print("This is the item to delete:", position)
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)