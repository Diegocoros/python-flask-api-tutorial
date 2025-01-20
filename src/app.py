from flask import Flask, jsonify
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]
@app.route('/todos', methods=['GET'])
def hello_world():
    # Puedes convertir esa variable en una cadena json de la siguiente manera
    json_text = jsonify(todos)

    # Y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return json_text

from flask import jsonify, request
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body) 
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    del todos[position]
    return jsonify(todos)
# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)