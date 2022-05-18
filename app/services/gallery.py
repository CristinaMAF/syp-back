""" Gallery Service """
import os
import cv2
import shutil

from flask import current_app as app
from app.models import GalleryModel
from werkzeug.utils import secure_filename


class GalleryService(object):
    """ Service for the Gallery entity """

    @staticmethod
    def add_photo(username, photo):
        existing_photos = GalleryModel.get_all_photos(username)
        if photo.filename not in existing_photos:
            user_dir = os.path.join(app.config.get("IMAGES_BASE_DIR"), username)
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(user_dir, filename))
            GalleryModel.add_photo(username, filename)
    
    # Method to take all photos from an user
    @staticmethod
    def get_gallery(username):
        return GalleryModel.get_gallery(username)

    # Method to update selected value on database
    @staticmethod
    def update_selected(id, selected):
        return GalleryModel.update_selected(id, selected)

    # Method to count the selected images
    @staticmethod
    def count_selected(username):
        return GalleryModel.count_selected(username)

    # Method to delete the directory when the owner user is deleted
    @staticmethod
    def delete_dir(username):
        user_dir = os.path.join(app.config.get("IMAGES_BASE_DIR"), username)
        shutil.rmtree(user_dir)
