from flask import Flask, request, jsonify, send_file, Blueprint, render_template
from app.database.db import db
from app.database.models.users_model import User

user_bp = Blueprint('users', __name__)

@user_bp.get('/api/users')
def get_users():
    try:
        users_list = User.query.all()
        result = [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email
            } 
            for user in users_list
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"Error": f"Error obtaining data: {str(e)}"}), 500

@user_bp.post('/api/users')
def create_user():
    data = request.get_json()
    
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )

    try:
        db.session.add(new_user) 
        db.session.commit()      
        
        return jsonify({
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }), 201
        
    except Exception as e:
        db.session.rollback() 
        return jsonify({"Error": str(e)}), 500

@user_bp.delete('/api/users/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    
    if not user:
        return jsonify({"Error": "User not found"}), 404
        
    try:
        deleted_data = {
            "id": user.id,
            "username": user.username
        }
        db.session.delete(user) 
        db.session.commit()    
        
        return jsonify({
            "message": "User deleted successfully",
            "deleted_data": deleted_data
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"Error": str(e)}), 500

@user_bp.put('/api/users/<int:id>')
def update_users(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"Error": "User not found"}), 404

    data = request.get_json()

    try: 
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        
        if 'password' in data and data['password']:
            user.password = data['password']

        db.session.commit() 

        updated_user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }

        return jsonify({
            "Message": "Changes have been made", 
            "User": updated_user_data
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"Error": str(e)}), 500

@user_bp.get('/api/users/<int:id>')
def get_user_selected(id):
    try:
        user = User.query.get(id)

        if user is None:
             return jsonify({'Message': 'User not found'}), 404

        result = {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"Error": str(e)}), 500

@user_bp.get('/')
def home():
    return render_template('index.html')
