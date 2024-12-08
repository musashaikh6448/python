from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/userDB"
mongo = PyMongo(app)
users_collection = mongo.db.users  # This references the 'users' collection

# Routes

# 1. Home - List users
@app.route('/')
def index():
    users = users_collection.find()
    return render_template('index.html', users=users)

# 2. Add user
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Insert new user to the collection
        users_collection.insert_one({'name': name, 'email': email})
        return redirect(url_for('index'))

    return render_template('add_user.html')

# 3. Edit user
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_user(id):
    user = users_collection.find_one({"_id": ObjectId(id)})

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Update user in the collection
        users_collection.update_one({"_id": ObjectId(id)}, {"$set": {'name': name, 'email': email}})
        return redirect(url_for('index'))

    return render_template('edit_user.html', user=user)

# 4. Delete user
@app.route('/delete/<id>')
def delete_user(id):
    users_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

# 5. API - Get all users
@app.route('/api/users', methods=['GET'])
def api_get_users():
    users = users_collection.find()
    user_list = [{"_id": str(user['_id']), "name": user['name'], "email": user['email']} for user in users]
    return jsonify(user_list)

# 6. API - Get single user
@app.route('/api/users/<id>', methods=['GET'])
def api_get_user(id):
    user = users_collection.find_one({"_id": ObjectId(id)})
    if user:
        return jsonify({"_id": str(user['_id']), "name": user['name'], "email": user['email']})
    return jsonify({"error": "User not found"}), 404

# 7. API - Add user
@app.route('/api/users', methods=['POST'])
def api_add_user():
    data = request.json
    users_collection.insert_one({'name': data['name'], 'email': data['email']})
    return jsonify({"message": "User created successfully"}), 201

# 8. API - Update user
@app.route('/api/users/<id>', methods=['PUT'])
def api_update_user(id):
    data = request.json
    users_collection.update_one({"_id": ObjectId(id)}, {"$set": {'name': data['name'], 'email': data['email']}})
    return jsonify({"message": "User updated successfully"}), 200

# 9. API - Delete user
@app.route('/api/users/<id>', methods=['DELETE'])
def api_delete_user(id):
    users_collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
