""" User entity """
from app import db
from app.models.gallery import Gallery
from sqlalchemy import event


class User(db.Model):
    """ Entity for saving the users"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    username = db.Column(db.String(16), unique= True)
    password = db.Column(db.String(16))


class UserModel(object):
    """ Model for performing operations on the entity User """

    @staticmethod
    def add_user(name, username, password):
        new_user = User(name=name, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id, "name": new_user.name, "username": new_user.username, "password": new_user.password}
    
    @staticmethod
    def get_all():
        return  [{"id": user.id, "name": user.name, "username": user.username, "password": user.password} for user in User.query.all() ] 

    @staticmethod
    def delete_user(username):   
        db.session.query(Gallery).filter_by(username= username).delete()    
        db.session.query(User).filter_by(username= username).delete() 
        db.session.commit()

    @staticmethod
    def get_user(username, password):
        return db.session.query(User).filter_by(username= username, password= password).all()


# Create an admin user on database inicialization
@event.listens_for(User.__table__, 'after_create')
def create_departments(*args, **kwargs):
    db.session.add(User(name='Admin', username='admin', password = 'admin22**'))
    db.session.commit()