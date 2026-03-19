from flask import Blueprint,request,jsonify
from main import PaymentModel,db

PaymentModel_bp=Blueprint("payment", __name__)

@PaymentModel_bp.route('/payment', methods=['POST'])
def create_payment():
    data = request.json

    payment = PaymentModel(
        order_id=data.get('order_id'),
        amount=data.get('amount'),
        payment_method=data.get('payment_method'),
        transaction_id=data.get('transaction_id'),
        remarks=data.get('remarks')
    )

    db.session.add(payment)
    db.session.commit()

    return jsonify(payment.to_dict())


@PaymentModel_bp.route('/payment', methods=['GET'])
def get_payments():
    payments = PaymentModel.query.filter_by(is_deleted=False).all()
    return jsonify([p.to_dict() for p in payments])


@PaymentModel_bp.route('/payment/<int:id>', methods=['GET'])
def get_payment(id):
    payment = PaymentModel.query.filter_by(id=id, is_deleted=False).first()

    if not payment:
        return jsonify({'message': 'Payment not found'})

    return jsonify(payment.to_dict())


@PaymentModel_bp.route('/payment/<int:id>', methods=['PUT'])
def update_payment(id):
    payment = PaymentModel.query.filter_by(id=id, is_deleted=False).first()

    if not payment:
        return jsonify({'message': 'Payment not found'})

    data = request.json

    payment.amount = data.get('amount', payment.amount)
    payment.payment_method = data.get('payment_method', payment.payment_method)
    payment.transaction_id = data.get('transaction_id', payment.transaction_id)
    payment.remarks = data.get('remarks', payment.remarks)

    db.session.commit()

    return jsonify(payment.to_dict())


@PaymentModel_bp.route('/payment/delete/<int:id>', methods=['PUT'])
def delete_payment(id):
    payment = PaymentModel.query.get(id)

    if not payment:
        return jsonify({'message': 'Payment not found'})

    payment.is_deleted = True
    db.session.commit()

    return jsonify({'message': 'Payment deleted successfully'})