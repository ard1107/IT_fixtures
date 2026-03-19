from flask import Blueprint, request, jsonify
from models import OrderItemModel
from models import *
OrderItemModel_bp = Blueprint('OrderItemModel_bp',(__name__))

@OrderItemModel_bp.route('/order-items', methods=['GET'])
def get_items():
    items = OrderItemModel.query.get_all_active()
    return jsonify([item.to_dict() for item in items])

#  POST (CREATE) 
@OrderItemModel_bp.route('/order-item', methods=['POST'])
def create_item():
    data = request.json()

# Create the object
    new_item = OrderItemModel(
        order_id=data['order_id'],
        product_id=data['product_id'],
        quantity=data['quantity'],
        price=data['price'],
        vender_id=data['vender_id']
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict())

# PUT (UPDATE) 
@OrderItemModel_bp.route('/order-item/<int:id>', methods=['PUT'])
def update_item(id):
    item = OrderItemModel.get_by_id(id)
    if not item:
        return jsonify({"error": "Item not found"})
    
    data = request.get_json()
    item.update_item(data)
    return jsonify(item.to_dict())

# DELETE (SOFT DELETE) 
@OrderItemModel_bp.route('/order-item/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = OrderItemModel.get_by_id(id)
    if not item:
        return jsonify({"error": "Item not found"})
    
    item.soft_delete()
    return jsonify({"message": "Item soft-deleted successfully"})

