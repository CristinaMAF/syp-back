# Select your photos API implementation

Lightweight Python Flask API for implementing the Slect your photos back.


# Getting Started


## Enviroment variables

The App needs to set the following variables:

* FLASK_APP: **(required)** run.py.
* JWTSECRETKEY: token generator
* IMAGES_BASE_DIR: directory for save the upload photos
* SQLALCHEMY_DATABASE_URI: database URL, if not specified a local sql-lite database will be used to avoid losing items due to an unexpected server shutdown.

## Intallation

This APP requires Python 3.X. In the App directory:

1. `$ git clone https://github.com/Develooser/syp-back.git`.
2. `cd syp-back`.
3. `$ pip install virtualenv` (if not installed).
4. `$ virtualenv venv`.
5. `$ .\venv\Scripts\activate.bat` | `source venv/bin/activate`.
6. `$ pip install -r requirements.txt`.
7. `$ set FLASK_APP=run.py` | `$ export FLASK_APP=run.py`.
8. `$ flask run`.
