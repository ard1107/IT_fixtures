from flask import Blueprint, request, jsonify
from datetime import datetime
from models import *

MediaFiles_blueprint = Blueprint("MediaFiles_blueprint", __name__)

@MediaFiles_blueprint.route("/createmediafiles", methods=["POST"])
def create_mediafile():
    data = request.get_json()
    media = MediaFiles(
        file_name = data["file_name"],
        file_url = data["file_url"],
        file_title = data["file_title"],
        file_type = data["file_type"],
        alt_text = data["alt_text"],
        entity_type = data["entity_type"],
        entity_id = data["vendor_id"],
       )
    db.session.add(media)
    db.session.commit()
    return jsonify({"message": "Media file created successfully" })

@MediaFiles_blueprint.route('/mediafiles', methods=["GET"])
def get_mediafiles():
    media = MediaFiles.query.all()
    return jsonify([m.to_dict_med() for m in media])

@MediaFiles_blueprint.route("/mediafiles/<int:id>", methods=["GET"])
def get_mediafiles_by_id(id):
    mediafiles = MediaFiles.query.all()
    users = Users.query.filter_by(id=Users.id).first()
    return jsonify([m.to_dict_med() for m in mediafiles])

@MediaFiles_blueprint.route('/update_mediafiles/<int:id>', methods=["PUT"])
def update_mediafiles(id):
    mediafiles = MediaFiles.query.filter_by(id=id).first()
    data = request.get_json()
    mediafiles.file_name = data["file_name"]
    mediafiles.file_url = data["file_url"]
    mediafiles.file_title = data["file_title"]
    mediafiles.file_type = data["file_type"]
    mediafiles.alt_text = data["alt_text"]
    mediafiles.entity_type = data["entity_type"]
    mediafiles.entity_id = data["entity_id"]
    db.session.commit()
    return jsonify({"message":"updated media file"})

@MediaFiles_blueprint.route('/delete_mediafiles', methods=["DELETE"])
def delete_mediafiles(id):
    mediafiles = MediaFiles.query.get(id)
    mediafiles.deleted_at = datetime.now
    db.session.commit()
    return({"message":"mediafiles deleted successfully"})