""" User Service """
from flask import current_app as app
from app.models import UserModel, GalleryModel
import os
import errno

from app.services.gallery import GalleryService


class UserService(object):
    """ Service for the User entity """

    @staticmethod
    def add_user(name, username, password):
       user = UserModel.add_user(name, username, password)
       user_dir = os.path.join(app.config.get("IMAGES_BASE_DIR"), username)
       os.makedirs(user_dir)
       return user
    
    @staticmethod
    def get_all():
        users = UserModel.get_all()

        for user in users:
            user["selectedPhotos"] = GalleryModel.count_selected(user.get("username"))
        
        return users


    @staticmethod
    def delete_user(username):
        delete_user= UserModel.delete_user(username)
        GalleryService.delete_dir(username)
        return delete_user


    @staticmethod
    def get_user(username, password):
        return UserModel.get_user(username, password)