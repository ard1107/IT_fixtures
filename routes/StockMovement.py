from flask import Blueprint, request, jsonify
from main import StockMovement,db

StockMovement=Blueprint('StockMovement')


@StockMovement.route('/add_Stock_Movement', methods=['POST'])
def add_stock_movement():
    data = request.get_json()
    new_stock_movement = StockMovement(
        product_id=data['product_id'],
        from_hub_id=data.get('from_hub_id'),
        to_hub_id=data.get('to_hub_id'),
        distributor_id=data.get('distributor_id'),
        quantity=data['quantity'],
        movement_type=data['movement_type'],
        vendor_id=data['vendor_id'],
        remarks=data.get('remarks'),
        responsible_user_id=data['responsible_user_id']
    )
    db.session.add(new_stock_movement)
    db.session.commit()
    return jsonify({'message': 'Stock movement added successfully', 'stock_movement': new_stock_movement.to_dict()})
    
@StockMovement.route('/update_Stock_Movement/<int:stock_movement_id>', methods=['PUT'])
def update_stock_movement(stock_movement_id):
    stock_movement = StockMovement.query.get(stock_movement_id)
    if not stock_movement:
        return jsonify({'message': 'Stock movement not found'}), 404

    data = request.get_json()
    stock_movement.status = data.get('status')
    stock_movement.remarks = data.get('remarks')

    db.session.commit()

    #update the stock quantity in the respective hubs after a stock movement
    stock_movement.update_stock()

    return jsonify({'message': 'Stock movement updated successfully', 'stock_movement': stock_movement.to_dict()})

@StockMovement.route('/get_all_stock_movement',methods=['GET'])
def get_all_stock_movement():
    data=StockMovement.query.all()
    return jsonify({'stock_movements': [stock_movement.to_dict() for stock_movement in data]})


@StockMovement.route('/get_by_id',methods=['GET'])
def get_by_id_allstock_movement(stock_movement_id):
    data=StockMovement.query.get(stock_movement_id)
    if not data:
        return jsonify({'message': 'Stock movement not found'}), 404
    return jsonify({'stock_movement': data.to_dict()})

@StockMovement.route('/delete_Stock_Movement/<int:stock_movement_id>', methods=['PUT'])
def delete_stock_movement(stock_movement_id):
    stock_movement = StockMovement.query.get(stock_movement_id)
    if not stock_movement:
        return jsonify({'message': 'Stock movement not found'}), 404

    db.session.delete(stock_movement)
    db.session.commit()

    return jsonify({'message': 'Stock movement deleted successfully'})



