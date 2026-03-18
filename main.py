from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/inventory_management'
db = SQLAlchemy(app)

class VendorDistributor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    distributor_id = db.Column(db.Integer, db.ForeignKey('distributor.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    UpdatedAt = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    DeletedAt = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'vendor_id': self.vendor_id,
            'distributor_id': self.distributor_id
        }
    

@app.route('/add_Vendor',methods=['POST'])
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

@app.route('/get_All_Vendor/',methods=['GET'])
def get_all_vendors():
    vendors = Vendors.query.all()
    return jsonify({'vendors': [vendor.to_dict() for vendor in vendors]})

@app.route('/get_Vendor/<int:vendor_id>',methods=['GET'])
def get_vendor(vendor_id):
    vendor = Vendors.query.get(vendor_id)
    if vendor:
        return jsonify({'vendor': vendor.to_dict()})
    else:
        return jsonify({'message': 'Vendor not found'})
    
@app.route('/update_Vendor/<int:vendor_id>', methods=['PUT'])
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
@app.route('/delete/',methods=['PUT'])
def Delete_Vendor(vendor_id):
    vendor = Vendors.query.get(vendor_id)
    if not vendor:
        return jsonify({'message': 'Vendor not found'})
    db.session.delete(vendor)
    db.session.commit()
    return jsonify({'message': 'Vendor deleted successfully'})

class Hubs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    hub_type = db.Column(db.String(50), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('hubs.id'), nullable=True)
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    UpdatedAt = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    DeletedAt = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address_id': self.address_id,
            'vendor_id': self.vendor_id,
            'hub_type': self.hub_type,
            'parent_id': self.parent_id if self.parent_id else None
        }
    
@app.route('/add_Hub',methods=['POST'])
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

@app.route('/get_All_Hub/',methods=['GET'])
def get_all_hubs():
    hubs = Hubs.query.all()
    return jsonify({'hubs': [hub.to_dict() for hub in hubs]})

@app.route('/get_Hub/<int:hub_id>',methods=['GET'])
def get_hub(hub_id):
    hub = Hubs.query.get(hub_id)
    if hub:
        return jsonify({'hub': hub.to_dict()})
    else:
        return jsonify({'message': 'Hub not found'})

@app.route('/update_Hub/<int:hub_id>', methods=['PUT'])
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

@app.route('/delete_Hub/<int:hub_id>',methods=['PUT'])
def delete_hub(hub_id):
    hub = Hubs.query.get(hub_id)
    if not hub:
        return jsonify({'message': 'Hub not found'}), 404

    db.session.delete(hub)
    db.session.commit()
    return jsonify({'message': 'Hub deleted successfully'})

class HubProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hub_id = db.Column(db.Integer, db.ForeignKey('hubs.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False) 
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    min_req_quantity = db.Column(db.Integer, nullable=True)
    max_stock_quantity = db.Column(db.Integer, nullable=True)
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    UpdatedAt = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    DeletedAt = db.Column(db.DateTime, nullable=True)
    def to_dict(self):
        return {
            'id': self.id,
            'hub_id': self.hub_id,
            'product_id': self.product_id,
            'vendor_id': self.vendor_id,
            'stock_quantity': self.stock_quantity,
            'min_req_quantity': self.min_req_quantity,
            'max_stock_quantity': self.max_stock_quantity
        }
    
@app.route('/add_Hub_Product', methods=['POST'])
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

@app.route('/update_Hub_Product/<int:hub_product_id>', methods=['PUT'])
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

@app.route('/delete_Hub_Product/<int:hub_product_id>', methods=['PUT'])
def delete_hub_product(hub_product_id):
    hub_product = HubProduct.query.get(hub_product_id)
    if not hub_product:
        return jsonify({'message': 'Hub product not found'}), 404

    db.session.delete(hub_product)
    db.session.commit()
    return jsonify({'message': 'Hub product deleted successfully'})

@app.route('/get_Hub_Product/<int:hub_product_id>', methods=['GET'])
def get_hub_product(hub_product_id):
    hub_product = HubProduct.query.get(hub_product_id)
    if hub_product:
        return jsonify({'hub_product': hub_product.to_dict()})
    else:
        return jsonify({'message': 'Hub product not found'})
    
@app.route('/get_All_Hub_Products/', methods=['GET'])
def get_all_hub_products():
    hub_products = HubProduct.query.all()
    return jsonify({'hub_products': [hub_product.to_dict() for hub_product in hub_products]})


class StockMovement(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    from_hub_id = db.Column(db.Integer, db.ForeignKey('hubs.id'), nullable=True)
    to_hub_id = db.Column(db.Integer, db.ForeignKey('hubs.id'), nullable=True)
    distributor_id = db.Column(db.Integer, db.ForeignKey('distributor.id'), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    movement_type = db.Column(db.String(50), nullable=False)  # 'transfer' or 'purchase'
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    remarks = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(20), nullable=False, default='inititated')  # 'inititated', 'in_transit', 'delivered', 'cancelled'
    responsible_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    UpdatedAt = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    DeletedAt = db.Column(db.DateTime, nullable=True)

#update the stock quantity in the respective hubs after a stock movement
    def update_stock(self):
        if self.movement_type == 'transfer' and self.status == 'delivered':
            from_hub_product = HubProduct.query.filter_by(hub_id=self.from_hub_id, product_id=self.product_id).first()
            to_hub_product = HubProduct.query.filter_by(hub_id=self.to_hub_id, product_id=self.product_id).first()

            if from_hub_product and to_hub_product:
                from_hub_product.stock_quantity -= self.quantity
                to_hub_product.stock_quantity += self.quantity
                db.session.commit()
        elif self.movement_type == 'purchase' and self.status == 'delivered':
            to_hub_product = HubProduct.query.filter_by(hub_id=self.to_hub_id, product_id=self.product_id).first()
            if to_hub_product:
                to_hub_product.stock_quantity += self.quantity
                db.session.commit()


    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'from_hub_id': self.from_hub_id,
            'to_hub_id': self.to_hub_id,
            'distributor_id': self.distributor_id,
            'quantity': self.quantity,
            'movement_type': self.movement_type,
            'vendor_id': self.vendor_id,
            'remarks': self.remarks,
            'responsible_user_id': self.responsible_user_id
        }
    

@app.route('/add_Stock_Movement', methods=['POST'])
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
    
@app.route('/update_Stock_Movement/<int:stock_movement_id>', methods=['PUT'])
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

@app.route('/get_all_stock_movement',methods=['GET'])
def get_all_stock_movement():
    data=StockMovement.query.all()
    return jsonify({'stock_movements': [stock_movement.to_dict() for stock_movement in data]})


@app.route('/get_by_id',methods=['GET'])
def get_by_id_allstock_movement(stock_movement_id):
    data=StockMovement.query.get(stock_movement_id)
    if not data:
        return jsonify({'message': 'Stock movement not found'}), 404
    return jsonify({'stock_movement': data.to_dict()})

@app.route('/delete_Stock_Movement/<int:stock_movement_id>', methods=['PUT'])
def delete_stock_movement(stock_movement_id):
    stock_movement = StockMovement.query.get(stock_movement_id)
    if not stock_movement:
        return jsonify({'message': 'Stock movement not found'}), 404

    db.session.delete(stock_movement)
    db.session.commit()

    return jsonify({'message': 'Stock movement deleted successfully'})

class StockMovementTrace(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_movement_id = db.Column(db.Integer, db.ForeignKey('stock_movement.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'inititated', 'in_transit', 'delivered', 'cancelled'
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    contact_person = db.Column(db.String(100), nullable=True)
    contact_number = db.Column(db.String(20), nullable=True)
    remarks = db.Column(db.String(500), nullable=True)
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    UpdatedAt = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    DeletedAt = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'stock_movement_id': self.stock_movement_id,
            'status': self.status,
            'timestamp': self.timestamp,
            'contact_person': self.contact_person,
            'contact_number': self.contact_number,
            'remarks': self.remarks
        }
@app.route('/add_Stock_Movement_Trace',methods=['POST'])
def add_stock_movement_trace():
    data = request.get_json()
    new_stock_movement_trace = StockMovementTrace(
        stock_movement_id=data['stock_movement_id'],
        status=data['status'],
        contact_person=data.get('contact_person'),
        contact_number=data.get('contact_number'),
        remarks=data.get('remarks')
    )
    db.session.add(new_stock_movement_trace)
    db.session.commit()
    return jsonify({'message': 'Stock movement trace added successfully', 'stock_movement_trace': new_stock_movement_trace.to_dict()})

@app.route('/update_Stock_Movement_Trace/<int:stock')
def update_stock_movement_trace(stock_movement_trace_id):
    stock_movement_trace = StockMovementTrace.query.get(stock_movement_trace_id)
    if not stock_movement_trace:
        return jsonify({'message': 'Stock movement trace not found'}), 404

    data = request.get_json()
    stock_movement_trace.status = data.get('status')
    stock_movement_trace.contact_person = data.get('contact_person')
    stock_movement_trace.contact_number = data.get('contact_number')
    stock_movement_trace.remarks = data.get('remarks')

    db.session.commit()
    return jsonify({'message': 'Stock movement trace updated successfully', 'stock_movement_trace': stock_movement_trace.to_dict()})


@app.route('/get_Stock_Movement_Trace/<int:stock_movement_id>', methods=['GET'])
def get_stock_movement_trace(stock_movement_id):
    traces = StockMovementTrace.query.filter_by(stock_movement_id=stock_movement_id).all()
    return jsonify({'stock_movement_traces': [trace.to_dict() for trace in traces]})

@app.route('/update_Stock_Movement_Trace/<int:stock_movement_trace_id>', methods=['PUT'])
def update_stock_movement_trace(stock_movement_trace_id):
    stock_movement_trace = StockMovementTrace.query.get(stock_movement_trace_id)
    if not stock_movement_trace:
        return jsonify({'message': 'Stock movement trace not found'}), 404

    data = request.get_json()
    stock_movement_trace.stock_movement_id = data.get('stock_movement_id', stock_movement_trace.stock_movement_id)
    stock_movement_trace.status = data.get('status', stock_movement_trace.status)
    stock_movement_trace.contact_person = data.get('contact_person', stock_movement_trace.contact_person)
    stock_movement_trace.contact_number = data.get('contact_number', stock_movement_trace.contact_number)
    stock_movement_trace.remarks = data.get('remarks', stock_movement_trace.remarks)

    db.session.commit()
    return jsonify({'message': 'Stock movement trace updated successfully', 'stock_movement_trace': stock_movement_trace.to_dict()})

@app.route('/delete_Stock_Movement_Trace/<int:stock_movement_trace_id>', methods=['DELETE'])
def delete_stock_movement_trace(stock_movement_trace_id):
    stock_movement_trace = StockMovementTrace.query.get(stock_movement_trace_id)
    if not stock_movement_trace:
        return jsonify({'message': 'Stock movement trace not found'}), 404

    db.session.delete(stock_movement_trace)
    db.session.commit()

    return jsonify({'message': 'Stock movement trace deleted successfully'})

















if __name__ == '__main__':
    with app.app_content():
        db.create_all()
    app.run(debug=True)


