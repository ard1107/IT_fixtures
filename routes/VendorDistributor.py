from flask import Blueprint, request, jsonify
from main import VendorDistributor,db


VendorDistributor=Blueprint('VendorDistributor')

@VendorDistributor.route('/add_Vendor', methods=['POST'])
def add_vendor():
    data = request.get_json()
    new_vendor = Vendors(
        business_name=data['business_name'],
        email=data['email'],
        mobile_number=data['mobile_number'],
        address_id=data['address_id']
    )
    db.session.add(new_vendor)
    db.session.commit()
    return jsonify({'message': 'Vendor added successfully', 'vendor': new_vendor.to_dict()})

@VendorDistributor.route('/get_All_Vendor/',methods=['GET'])
def get_all_vendors():
    vendors = Vendors.query.all()
    return jsonify({'vendors': [vendor.to_dict() for vendor in vendors]})

@VendorDistributor.route('/get_Vendor/<int:vendor_id>',methods=['GET'])
def get_vendor(vendor_id):
    vendor = Vendors.query.get(vendor_id)
    if vendor:
        return jsonify({'vendor': vendor.to_dict()})
    else:
        return jsonify({'message': 'Vendor not found'})
    
@VendorDistributor.route('/update_Vendor/<int:vendor_id>', methods=['PUT'])
def update_vendor(vendor_id):
    vendor = Vendors.query.get(vendor_id)
    if not vendor:
        return jsonify({'message': 'Vendor not found'}), 404

    data = request.get_json()
    vendor.business_name = data.get('business_name')
    vendor.email = data.get('email')
    vendor.mobile_number = data.get('mobile_number')

    db.session.commit()
    return jsonify({'message': 'Vendor updated successfully', 'vendor': vendor.to_dict()})

@VendorDistributor.route('/delete/',methods=['PUT'])
def Delete_Vendor(vendor_id):
    vendor = Vendors.query.get(vendor_id)
    if not vendor:
        return jsonify({'message': 'Vendor not found'})
    db.session.delete(vendor)
    db.session.commit()
    return jsonify({'message': 'Vendor deleted successfully'})

