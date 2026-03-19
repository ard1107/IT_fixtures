from flask import Blueprint, app, request, jsonify
from models import PaymentModel 
from models import *
PaymentModel_bp= Blueprint('PaymentModel_bp',(__name__)) 

@PaymentModel_bp.route('/payment', methods=['POST'])
def create_payment():
    data = request.json
    obj = PaymentModel(
        order_id=data['order_id'],
        amount=data['amount'],
        payment_method=data['payment_method'],
        transaction_id=data.get('transaction_id')
    )
    db.session.add(obj)
    db.session.commit()
    return jsonify(obj.to_dict())
                   
@PaymentModel_bp.route('/payment', methods=['GET'])
def get_payments():

    data = PaymentModel.query.filter_by(is_deleted=False).all()
    return jsonify([i.to_dict() for i in data])

@PaymentModel_bp.route('/payment/<int:id>', methods=['GET'])
def get_payment(id):

    obj = PaymentModel.query.filter_by(id=id, is_deleted=False).first()
    return jsonify(obj.to_dict())

@PaymentModel_bp.route('/payment/<int:id>', methods=['PUT'])
def update_payment(id):
    data = request.json
    obj = PaymentModel.query.get(id)
    obj.amount = data.get('amount', obj.amount)
    obj.payment_method = data.get('payment_method', obj.payment_method)
    db.session.commit()
    return jsonify(obj.to_dict())

@PaymentModel_bp.route('/payment/<int:id>', methods=['DELETE'])
def delete_payment(id):

    obj = PaymentModel.query.get(id)
    obj.is_deleted = True
    db.session.commit() 
    return jsonify({"message": "Deleted"})