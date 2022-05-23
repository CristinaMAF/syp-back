""" Application config variables. """
import os


# Ensure the app.db file will be in the App directory
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """ Class for linking the config variables to Flask. """

    # SQL Alchemy
    JWT_SECRET_KEY = 'Select-your-photos'
    ADMIN_USER = 'admin'
    IMAGES_BASE_DIR = os.path.join(basedir, 'resources', 'images')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f"sqlite:///{os.path.join(basedir, 'app.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
