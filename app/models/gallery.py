"""Gallery entity  """

from email.policy import default
from app import db


class Gallery(db.Model):
   """Entity for saving the galleries"""
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(16))
   photoname = db.Column(db.String(32), unique= True)
   selected = db.Column(db.Boolean, default= False)

class GalleryModel(object):
    @staticmethod
    def add_photo(username, photoname):
        new_photo = Gallery(username=username, photoname=photoname)
        db.session.add(new_photo)
        db.session.commit()
        return {"id": new_photo.id, "username": new_photo.username, "photoname": new_photo.photoname}

    @staticmethod
    def get_gallery(username):
        return db.session.query(Gallery.photoname).filter_by(username= username).all()
