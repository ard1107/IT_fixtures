from flask import Blueprint, request, jsonify
from main import Hubs,db

Hubs=Blueprint('Hubs')

@Hubs.route('/add_Hub', methods=['POST'])
def add_hub():
    data = request.get_json()
    new_hub = Hubs(
        name=data['name'],
        description=data['description'],
        hub_type=data['hub_type'],
        address_id=data['address_id'],
        vendor_id=data['vendor_id'],
        parent_id=data.get('parent_id')
    )
    db.session.add(new_hub)
    db.session.commit()
    return jsonify({'message': 'Hub added successfully', 'hub': new_hub.to_dict()})

@Hubs.route('/get_All_Hub/',methods=['GET'])
def get_all_hubs():
    hubs = Hubs.query.all()
    return jsonify({'hubs': [hub.to_dict() for hub in hubs]})

@Hubs.route('/get_Hub/<int:hub_id>',methods=['GET'])
def get_hub(hub_id):
    hub = Hubs.query.get(hub_id)
    if hub:
        return jsonify({'hub': hub.to_dict()})
    else:
        return jsonify({'message': 'Hub not found'})

@Hubs.route('/update_Hub/<int:hub_id>', methods=['PUT'])
def update_hub(hub_id):
    hub = Hubs.query.get(hub_id)
    if not hub:
        return jsonify({'message': 'Hub not found'}), 404

    data = request.get_json()
    hub.name = data.get('name')
    hub.description = data.get('description')
    hub.hub_type = data.get('hub_type')
    hub.address_id = data.get('address_id')
    hub.parent_id = data.get('parent_id')

    db.session.commit()
    return jsonify({'message': 'Hub updated successfully', 'hub': hub.to_dict()})

@Hubs.route('/delete_Hub/<int:hub_id>',methods=['PUT'])
def delete_hub(hub_id):
    hub = Hubs.query.get(hub_id)
    if not hub:
        return jsonify({'message': 'Hub not found'}), 404

    db.session.delete(hub)
    db.session.commit()
    return jsonify({'message': 'Hub deleted successfully'})
