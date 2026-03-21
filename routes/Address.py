from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Address
from models import db
Address_blueprint = Blueprint("Address_blueprint", __name__)

@Address_blueprint.route('/createaddress', methods=["POST"])
def create_address():
    data = request.get_json()
    address = Address (
                        address_line1 = data["address_line1"],
                        address_line2 = data["address_line2"],
                        address_line3 = data["address_line3"],
                        landmark = data["landmark"],
                        city = data["city"],
                        state = data["state"],
                        postal_code = data["postal_code"],
                        country = data["country"],
                        lat_lang = data["lat_lang"],
                        google_map_address = data["google_map"]  
                        )
    db.session.add(address)
    db.session.commit()
    return jsonify({"message": "address added successfully"})

@Address_blueprint.route('/address', methods=["GET"])
def get_address():
    address = Address.query.all()
    return jsonify([a.to_dict_add() for a in address])

@Address_blueprint.route('/address_id/<int:id>' , methods=["GET"])
def get_address_id(id):
    add = Address.query.filter_by(id=id).first()
    return jsonify([add.to_dict_add()])

@Address_blueprint.route('/update_address/<int:id>', methods=["PUT"])
def update_address(id):
    address = Address.query.filter_by(id=id).first()
    data = request.get_json()
    address.address_line1 = data["address_line1"]
    address.address_line2 = data["address_line2"]
    address.address_line3 = data["address_line3"]
    address.landmark = data["landmark"]
    address.city = data["city"]
    address.state = data["state"]
    address.postal_code = data["postal_code"]
    address.country = data["country"]
    address.lat_lang = data["lat_lang"]
    address.google_map = data["google_map"]
    db.session.commit()
    return jsonify({"message": "address updated successfully"})

@Address_blueprint.route('/delete_address/<int:id>' ,methods=["DELETE"])
def delete_address(id):
    address = Address.query.get(id)
    address.delete_at = datetime.now
    db.session.commit()
    return jsonify({"message": "address deleted successfully"})