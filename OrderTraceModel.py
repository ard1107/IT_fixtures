from flask import Blueprint, request, jsonify
from models import OrderTraceModel
from models import *
OrderTraceModel_bp = Blueprint('OrderTraceModel_bp',(__name__))  
#create
@OrderTraceModel_bp.route('/order_trace', methods=['POST'])
def create_order_trace():
    data = request.json
    order_trace = OrderTraceModel(
        status=data.get('status'),
        track_url=data.get('track_url'),
        remarks=data.get('remarks')
    )
    db.session.add(order_trace)
    db.session.commit()
    return jsonify(order_trace.to_dict())

# GET ALL
@OrderTraceModel_bp.route('/order_trace', methods=['GET'])
def get_all_order_trace():
    data = OrderTraceModel.query.all()
    return jsonify([i.to_dict() for i in data])

# GET BY ID8
@OrderTraceModel_bp.route('/order_trace_id/<int:id>', methods=['GET'])
def get_order_trace(id):
    data = OrderTraceModel.query.filter_by(d=id).first()
    return jsonify(data.to_dict())

# UPDATE
@OrderTraceModel_bp.route('/order-trace/<int:id>', methods=['PUT'])
def update_order_trace(id):
    data = request.json
    obj = OrderTraceModel.query.get(id)

    obj.status = data.get('status', obj.status)
    obj.track_url = data.get('track_url', obj.track_url)
    obj.remarks = data.get('remarks', obj.remarks)

    db.session.commit()
    return jsonify(obj.to_dict())

# SOFT DELETE
@OrderTraceModel_bp.route('/order-trace/<int:id>', methods=['PUT'])
def delete_order_trace(id):
    obj = OrderTraceModel.query.get(id)
    obj.is_deleted = True
    db.session.commit()
    return jsonify({"message": "Deleted successfully"})

@OrderTraceModel_bp.route('/order-history/<int:order_id>', methods=['GET'])
def get_order_history(order_id):
    history = OrderTraceModel.query.filter_by(order_id=order_id).all()
    return jsonify([trace.to_dict() for trace in history])