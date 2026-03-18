from flask import Blueprint, request, jsonify
from main import HubProduct,db

@HubProduct.route('/add_Hub_Product', methods=['POST'])
def add_hub_product():
    data = request.get_json()
    new_hub_product = HubProduct(
        hub_id=data['hub_id'],
        product_id=data['product_id'],
        vendor_id=data['vendor_id'],
        stock_quantity=data['stock_quantity'],
        min_req_quantity=data.get('min_req_quantity'),
        max_stock_quantity=data.get('max_stock_quantity')
    )
    db.session.add(new_hub_product)
    db.session.commit()
    return jsonify({'message': 'Hub product added successfully', 'hub_product': new_hub_product.to_dict()})

@HubProduct.route('/update_Hub_Product/<int:hub_product_id>', methods=['PUT'])
def update_hub_product(hub_product_id):
    hub_product = HubProduct.query.get(hub_product_id)
    if not hub_product:
        return jsonify({'message': 'Hub product not found'}), 404

    data = request.get_json()
    hub_product.stock_quantity = data.get('stock_quantity')
    hub_product.min_req_quantity = data.get('min_req_quantity')
    hub_product.max_stock_quantity = data.get('max_stock_quantity')

    db.session.commit()
    return jsonify({'message': 'Hub product updated successfully', 'hub_product': hub_product.to_dict()})

@HubProduct.route('/delete_Hub_Product/<int:hub_product_id>', methods=['PUT'])
def delete_hub_product(hub_product_id):
    hub_product = HubProduct.query.get(hub_product_id)
    if not hub_product:
        return jsonify({'message': 'Hub product not found'}), 404

    db.session.delete(hub_product)
    db.session.commit()
    return jsonify({'message': 'Hub product deleted successfully'})

@HubProduct.route('/get_Hub_Product/<int:hub_product_id>', methods=['GET'])
def get_hub_product(hub_product_id):
    hub_product = HubProduct.query.get(hub_product_id)
    if hub_product:
        return jsonify({'hub_product': hub_product.to_dict()})
    else:
        return jsonify({'message': 'Hub product not found'})
    
@HubProduct.route('/get_All_Hub_Products/', methods=['GET'])
def get_all_hub_products():
    hub_products = HubProduct.query.all()
    return jsonify({'hub_products': [hub_product.to_dict() for hub_product in hub_products]})
