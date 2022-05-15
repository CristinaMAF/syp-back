"""Gallery entity  """

from email.policy import default
from select import select
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
    def get_all_photos(username):
        return [gallery.photoname for gallery in db.session.query(Gallery).filter_by(username= username).all()]

    @staticmethod
    def get_gallery(username):
        return [{"id": gallery.id, "username": gallery.username, "photoname": gallery.photoname, "selected": gallery.selected} for gallery in db.session.query(Gallery).filter_by(username= username).all()]


    @staticmethod
    def update_selected(id, selected):
        db.session.query(Gallery).filter_by(id= id).update({"selected": selected}) 
        db.session.commit()

    @staticmethod
    def count_selected(username):
        return db.session.query(Gallery).filter_by(username=username, selected=True).count()