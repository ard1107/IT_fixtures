from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Product, db
Product_blueprint = Blueprint("Product_blueprint", __name__)


@Product_blueprint.route('/createproduct', methods=["POST"])
def create_products():
    data = request.get_json()
    products = Product (
                     name = data["name"],
                     description = data["description"],
                     price = data["price"],
                     sku_id = data["sku_id"],
                     barcode = data["barcode"],
                     brand_id = data["brand_id"],
                     vendor_id = data["vendor_id"],
                     product_type = data["product_type"]
                      )
    db.session.add(products)
    db.session.commit()
    return({"message": "product added successfully"})

@Product_blueprint.route('/products', methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict_pro() for p in products])

@Product_blueprint.route('/product_id/<int:id>', methods=["GET"])
def get_product(id):
    products = Product.query.filter_by(id=id).first()
    return jsonify([products.to_dict_pro()])

@Product_blueprint.route('/update_products/<int:id>', methods=["PUT"])
def update_produts(id):
    products = Product.query.filter_by(id=id).first()
    data = request.get_json()
    products.name = data["name"]
    products.description = data["description"]
    products.price = data["price"]
    products.sku_id = data["barcode"]
    products.barcode = data["barcode"]
    products.product = data["product_type"]
    db.session.commit()
    return({"message":"updated successfully"})

@Product_blueprint.route('/delete_products', methods=["DELETE"])
def delete_products(id):
    products = Product.query.get(id)
    products.deleted_at = datetime.now()
    db.session.commit()
    return jsonify({"message":"product deleted successfully"})