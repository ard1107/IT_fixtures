from flask import Blueprint,request,jsonify
from main import OrderModel,db

OrderModel_bp=Blueprint("order", __name__)

@OrderModel_bp.route('/order', methods=['POST'])
def create_order():
    data = request.json

    order = OrderModel(
        user_id=data.get('user_id'),
        total_amount=data.get('total_amount'),
        delivery_address_id=data.get('delivery_address_id'),
        hub_id=data.get('hub_id'),
        status=data.get('status'),
        vendor_id=data.get('vendor_id'),
        delivery_partner_id=data.get('delivery_partner_id')
    )

    db.session.add(order)
    db.session.commit()

    return jsonify(order.to_dict())


@OrderModel_bp.route('/order', methods=['GET'])
def get_orders():
    orders = OrderModel.query.filter_by(is_deleted=False).all()
    return jsonify([o.to_dict() for o in orders])


@OrderModel_bp.route('/order/<int:id>', methods=['GET'])
def get_order(id):
    order = OrderModel.query.filter_by(id=id, is_deleted=False).first()

    if not order:
        return jsonify({'message': 'Order not found'})

    return jsonify(order.to_dict())


@OrderModel_bp.route('/order/<int:id>', methods=['PUT'])
def update_order(id):
    order = OrderModel.query.filter_by(id=id, is_deleted=False).first()

    if not order:
        return jsonify({'message': 'Order not found'})

    data = request.json

    order.total_amount = data.get('total_amount', order.total_amount)
    order.status = data.get('status', order.status)
    order.hub_id = data.get('hub_id', order.hub_id)
    order.delivery_partner_id = data.get('delivery_partner_id', order.delivery_partner_id)

    db.session.commit()

    return jsonify(order.to_dict())


@OrderModel_bp.route('/order/delete/<int:id>', methods=['PUT'])
def delete_order(id):
    order = OrderModel.query.get(id)

    if not order:
        return jsonify({'message': 'Order not found'})

    order.is_deleted = True
    db.session.commit()

    return jsonify({'message': 'Order deleted successfully'})