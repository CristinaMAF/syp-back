""" Game Service """
from flask import current_app as app
from app.models import UserModel


class UserService(object):
    """ Service for the User entity """

    @staticmethod
    def add_user(name, username, password):
       return UserModel.add_user(name, username, password)
    
    @staticmethod
    def get_all():
        return UserModel.get_all()

    @staticmethod
    def get_user(username, password):
        return UserModel.get_user(username, password)