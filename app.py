from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (no database)
todos = []

# Create


@app.route("/todo", methods=["POST"])
def create_todo():
    data = request.get_json()
    todos.append(data)
    return jsonify({"status": "created", "todo": data}), 201

# Read all
@app.route("/todo", methods=["GET"])
def get_todos():
    return jsonify(todos), 200

# Update
@app.route("/todo/<int:index>", methods=["PUT"])
def update_todo(index):
    if index >= len(todos):
         return jsonify({"error": "Not found"}), 404

    data = request.get_json()
    todos[index] = data
    return jsonify({"status": "updated", "todo": data}), 200

# Delete
@app.route("/todo/<int:index>", methods=["DELETE"])
def delete_todo(index):
    if index >= len(todos):
        return jsonify({"error": "Not found"}), 404

    deleted = todos.pop(index)
    return jsonify({"status": "deleted", "todo": deleted}), 200


@app.route("/")
def home():
    return jsonify({"message": "Simple Flask CRUD with CI is working!"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5050)