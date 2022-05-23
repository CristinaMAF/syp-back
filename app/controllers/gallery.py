""" Base application's controller for gallery interaction """
import os

from flask import request, jsonify, send_file
from flask import current_app as app
from app.controllers import endpoint_bp
from app.services import GalleryService
from flask_jwt_extended import jwt_required


@endpoint_bp.route('/backend/gallery/new', methods=['POST'])
@jwt_required()
def add_photo():
    photo = request.files['file']
    username = request.form['username']

    if username and photo:
        GalleryService.add_photo(username, photo)
        return {}, 200
    else:
        return "Bad request: missing user.", 400

@endpoint_bp.route('/backend/gallery/all/<string:username>', methods=['GET'])
@jwt_required()
def get_gallery(username):
    return jsonify(GalleryService.get_gallery(username)), 200

@endpoint_bp.route('/backend/gallery/<string:username>/<string:photoname>')
def get_image(username, photoname):
    photo_path = os.path.join(app.config.get("IMAGES_BASE_DIR"), username, photoname)
    return send_file(photo_path, mimetype='image')


@endpoint_bp.route('/backend/gallery/select', methods=['POST'])
@jwt_required()
def update_selected():
    content = request.json
    if content.get('id') and content.get('selected') is not None:
        GalleryService.update_selected(content.get('id'), content.get('selected'))
    return {}, 200
