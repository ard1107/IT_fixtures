from flask import Blueprint,request,jsonify 
from app import DeliveryPartner           

DeliveryPartnerModel_bp = Blueprint("DeliveryPartnerModel_bp",(__name__))



@delivery_bp.route('/delivery-partner', methods=['POST'])
def create_delivery_partner():
    data = request.json
    obj = DeliveryPartnerModel(
        name=data['name'],
        email=data['email'],
        mobile_number=data['mobile_number'],
        address_id=data['address_id'],
        vendor_id=data['vendor_id']
    )
    db.session.add(obj)
    db.session.commit()
    return jsonify(obj.to_dict())

@delivery_bp.route('/delivery-partner', methods=['GET'])
def get_delivery_partners():
    data = DeliveryPartnerModel.query.filter_by(is_deleted=False).all()
    return jsonify([i.to_dict() for i in data])

@delivery_bp.route('/delivery-partner/<int:id>', methods=['GET'])
def get_delivery_partner(id):
    obj = DeliveryPartnerModel.query.filter_by(id=id, is_deleted=False).first()
    return jsonify(obj.to_dict())

@delivery_bp.route('/delivery-partner/<int:id>', methods=['PUT'])
def update_delivery_partner(id):
    data = request.json
    obj = DeliveryPartnerModel.query.get(id)

    obj.name = data.get('name', obj.name)
    obj.email = data.get('email', obj.email)

    db.session.commit()
    return jsonify(obj.to_dict())

@delivery_bp.route('/delivery-partner/<int:id>', methods=['PUT'])
def delete_delivery_partner(id):
    obj = DeliveryPartnerModel.query.get(id)
    obj.is_deleted = True
    db.session.commit()
    return jsonify({"message": "Deleted"})  