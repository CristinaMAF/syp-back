""" Base application's controller for user interaction """
from flask import request, jsonify
from app.controllers import endpoint_bp
from app.services import UserService
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import current_app as app

    

@endpoint_bp.route('/backend/user/new', methods=['PUT'])
@jwt_required()
def add_user():
    content = request.json

    if content.get('name') and content.get('username') and content.get('password'):
        user = UserService.add_user(content.get('name'), content.get('username'), content.get('password'))
        return jsonify(user), 200
    else:
        return "Bad request: missing user.", 400

@endpoint_bp.route('/backend/user/token/validate', methods=['GET'])
@jwt_required()
def check_token():
    current_user = get_jwt_identity()

    return jsonify(username=current_user, isAdmin=current_user == app.config.get("ADMIN_USER")), 200

@endpoint_bp.route('/backend/user/all', methods=['GET'])
@jwt_required()
def get_all():
    return jsonify(UserService.get_all()), 200

@endpoint_bp.route('/backend/user/delete/<string:username>', methods=['DELETE'])
@jwt_required()
def delete_user(username):

    if username:
        UserService.delete_user(username)
        return {}, 200
    else:
        return "Bad request: missing username.", 400


@endpoint_bp.route('/backend/login', methods=['POST'])
def login():
    content = request.json

    if content and content.get('username') and content.get('password'):
        user = UserService.get_user(content.get('username'), content.get('password'))
        
        if user:
            user["token"] = create_access_token(identity=user.get("username"))
            return jsonify(user), 200
        else:
            return "Ususario o contraseña inválidos", 401
    else:
        return "Bad request: missing user.", 400
