from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Users
from models import db
Users_blueprint = Blueprint("Users_blueprint", __name__)

@Users_blueprint.route('/createuser', methods=['POST'])
def create_user():
    payload = request.get_json()
    users = Users(
        name = payload["name"],
        email = payload["email"],
        mobile_number = payload["mobile_number"],
        password = payload["password"],
        role = payload["role"],
        status = payload["status"]
    )
    db.session.add(users)
    db.session.commit()
    return jsonify({"message": "User created successfully"})

@Users_blueprint.route('/get',methods=['GET'])
def get_users():
    users = Users.query.all()
    return jsonify([user.to_dict() for user in users])

@Users_blueprint.route('/user/<int:id>', methods=["GET"])
def get_user_id(id):
    user = Users.query.filter_by(id=id).first()
    return jsonify(user.to_dict())

@Users_blueprint.route('/update_users/<int:id>', methods=["PUT"])
def update_user(id):
    users = Users.query.filter_by(id=id).first()
    data = request.get_json()
    users.name = data["name"]
    users.mobile_number = data["mobile_number"]
    users.email = data["email"]
    users.password = data["password"]
    users.role = data["role"]
    users.status = data["status"]
    db.session.commit()
    return jsonify({"message": "updated successfully"})
    
@Users_blueprint.route('/delete_users/<int:id>', methods=["DELETE"])
def delete_user(id):
    user = Users.query.get(id)
    user.deleted_at = datetime.now()
    db.session.commit()
    return({"message":"deleted successfully"})
