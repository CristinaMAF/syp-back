""" Gallery Service """
from flask import current_app as app
from app.models import GalleryModel

class GalleryService(object):
    """ Service for the Gallery entity """

    @staticmethod
    def add_photo(username, photoname):
       return GalleryModel.add_photo(username, photoname)
    

    @staticmethod
    def get_gallery(username):
        return GalleryModel.get_gallery(username)