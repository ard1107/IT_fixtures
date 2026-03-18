from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Vendors
from models import db
Vendors_blueprint = Blueprint("Vendors_blueprint", __name__)

@Vendors_blueprint.route('/createvendors', methods=["POST"])
def create_vendors():
    data = request.get_json()
    vendors = Vendors(
                       bussiness_name = data["bussiness_name"],
                       email = data["email"],
                       mobile_number = data["mobile_number"],
                       address_id = data["address_id"]
                     )
    db.session.add(vendors)
    db.session.commit()
    return jsonify({"message":"vendors added successfully"})

@Vendors_blueprint.route('/vendors', methods=["GET"])
def get_vendors():
    vendors = Vendors.query.all()
    return jsonify([v.to_dict_ven() for v in vendors])

@Vendors_blueprint.route('/vendor/<int:id>', methods=["GET"])
def get_vendors_id(id):
    vendors = Vendors_blueprint.query.filter_by

@Vendors_blueprint.route('/update_vendors', methods=["PUT"])
def update_vendors(id):
    vendors = Vendors.query.filter_by(id=id).first()
    data = request.get_json()
    vendors.bussiness_name = data["bussiness_name"]
    vendors.email = data["email"]
    vendors.mobile_number = data["mobile_number"]
    vendors.address_id = data["address_id"]

@Vendors_blueprint.route('/delete_vendors', methods=["DELETE"])
def delete_vendors(id):
    vendors = Vendors.query.get(id)
    vendors.deleted_at = datetime.now
    db.session.commit()
    return({"message":"vendors deleted successfully"})