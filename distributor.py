from flask import Blueprint,request,jsonify
from main import Distributor,db

Distributor_bp=Blueprint("Distributor_bp",__name__)

@Distributor_bp.route('/distributor', methods=['POST'])
def create_distributor():
    data = request.json

    distributor = Distributor(
        name=data.get('name'),
        email=data.get('email'),
        mobile_number=data.get('mobile_number'),
        address_id=data.get('address_id'),
        vendor_id=data.get('vendor_id')
    )

    db.session.add(distributor)
    db.session.commit()

    return jsonify(distributor.to_dict())


@Distributor_bp.route('/distributor', methods=['GET'])
def get_all_distributors():
    distributors = Distributor.query.filter_by(is_deleted=False).all()
    return jsonify([d.to_dict() for d in distributors])


@Distributor_bp.route('/distributor/<int:id>', methods=['GET'])
def get_distributor(id):
    distributor = Distributor.query.filter_by(id=id, is_deleted=False).first()

    if not distributor:
        return jsonify({'message': 'Distributor not found'})

    return jsonify(distributor.to_dict())


@Distributor_bp.route('/distributor/<int:id>', methods=['PUT'])
def update_distributor(id):
    distributor = Distributor.query.filter_by(id=id, is_deleted=False).first()

    if not distributor:
        return jsonify({'message': 'Distributor not found'})

    data = request.json

    distributor.name = data.get('name', distributor.name)
    distributor.email = data.get('email', distributor.email)
    distributor.mobile_number = data.get('mobile_number', distributor.mobile_number)
    distributor.address_id = data.get('address_id', distributor.address_id)
    distributor.vendor_id = data.get('vendor_id', distributor.vendor_id)

    db.session.commit()

    return jsonify(distributor.to_dict())


@Distributor_bp.route('/distributor/delete/<int:id>', methods=['PUT'])
def delete_distributor(id):
    distributor = Distributor.query.get(id)

    if not distributor:
        return jsonify({'message': 'Distributor not found'})

    distributor.is_deleted = True
    db.session.commit()

    return jsonify({'message': 'Distributor deleted successfully'})