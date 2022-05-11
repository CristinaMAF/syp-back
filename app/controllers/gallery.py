""" Base application's controller for gallery interaction """
from flask import request, jsonify
from app.controllers import endpoint_bp
from app.services import GalleryService


@endpoint_bp.route('/backend/gallery/new', methods=['POST'])
def add_photo():
    content = request.json
    file = request.files['file']
    username = request.form['username']

    if username and file:
        photo = GalleryService.add_photo(content.get('username'), content.get('photoname'))
        return jsonify(photo), 200
    else:
        return "Bad request: missing user.", 400

@endpoint_bp.route('/backend/gallery/all', methods=['GET'])
def get_gallery():
    return jsonify(GalleryService.get_gallery()), 200