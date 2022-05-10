""" Base application's controller for games interaction """
from flask import request, jsonify
from app.controllers import endpoint_bp
from app.services import UserService


@endpoint_bp.route('/user/new', methods=['PUT'])
def add_user():
    content = request.json

    if content.get('name') and content.get('username') and content.get('password'):
        user = UserService.add_user(content.get('name'), content.get('username'), content.get('password'))
        return jsonify(user), 200
    else:
        return "Bad request: missing user.", 400

@endpoint_bp.route('/user/all', methods=['GET'])
def get_all():
    return jsonify(UserService.get_all()), 200



@endpoint_bp.route('/login', methods=['POST'])
def login():
    content = request.json

    if content and content.get('username') and content.get('password'):
        user = UserService.get_user(content.get('username'), content.get('password'))
        
        if user: 
            return {}, 200
        else:
            return "Ususario o contraseña inválidos", 401
    else:
        return "Bad request: missing user.", 400
