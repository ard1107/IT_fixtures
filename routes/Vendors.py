from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Vendors, Address, db
from opentelemetry import trace
tracer = trace.get_tracer(__name__)
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
    vendor = Vendors.query.get(id)

    if vendor is None:
        return jsonify({
            "status": "error",
            "message": f"Vendor with id {id} not found"
        }), 404

    return jsonify({
        "status": "success",
        "data": vendor.to_dict_ven()
    })
@Vendors_blueprint.route('/update_vendors/<int:id>', methods=["PUT"])
def update_vendors(id):
    vendor = Vendors.query.filter_by(id=id).first()
    data = request.get_json()
    vendor.bussiness_name = data["bussiness_name"]
    vendor.email = data["email"]
    vendor.mobile_number = data["mobile_number"]
    vendor.address_id = data["address_id"]
    db.session.commit()
    return jsonify({"message":"vendors update successfully"})

@Vendors_blueprint.route('/delete_vendors', methods=["DELETE"])
def delete_vendors(id):
    vendors = Vendors.query.get(id)
    vendors.deleted_at = datetime.now
    db.session.commit()
    return({"message":"vendors deleted successfully"})