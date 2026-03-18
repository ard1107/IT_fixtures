from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_number = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=True)
    role = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    vendorId = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'mobileNumber': self.mobile_number,
            'password': self.password,
            'role': self.role, 
            'status': self.status,
            'vendorId': self.vendorId
        }
    

class Vendors(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    business_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_number = db.Column(db.Integer, unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)


    def to_dict_ven(self):
        return {
            'id': self.id,
            'business_name': self.business_name,
            'email': self.email,
            'mobileNumber': self.mobile_number,
            'address': self.address
        }

class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=True)
    address_line1 = db.Column(db.String(200), nullable=False)
    address_line2 = db.Column(db.String(200), nullable=True)
    address_line3 = db.Column(db.String(200), nullable=True)
    landmark = db.Column(db.String(200), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    lat_lang = db.Column(db.String(100), nullable=True)
    google_map_address = db.Column(db.String(255), nullable=True)

    def to_dict_add(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'vendor_id': self.vendor_id,
            'address_line1': self.address_line1,
            'address_line2': self.address_line2,
            'address_line3': self.address_line3,
            'landmark': self.landmark,
            'city': self.city,
            'state': self.state,
            'postal_code': self.postal_code,
            'country': self.country,
            'lat_lang': self.lat_lang,
            'google_map_address': self.google_map_address
        }
    
class MediaFiles(db.Model):
    __tablename__ = 'mediafiles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=True)
    file_name = db.Column(db.String(200), nullable=False)
    file_url = db.Column(db.String(500), nullable=False)
    file_title = db.Column(db.String(100),nullable=True)
    file_type = db.Column(db.String(100),nullable= False)
    alt_text = db.Column(db.String(200), nullable=True)
    entity_type = db.Column(db.String(50), nullable=False)
    entity_id = db.Column(db.Integer, nullable=False)

    def to_dict_med(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'vendor_id': self.vendor_id,
            'file_name': self.file_name,
            'file_url': self.file_url,
            'file_title': self.file_title,
            'file_type': self.file_type,
            'alt_text': self.alt_text,
            'entity_type': self.entity_type,
            'entity_id': self.entity_id
        }
    
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    sku_id = db.Column(db.String(100), unique=True, nullable=False)
    barcode = db.Column(db.String(100), unique=True, nullable=True)
    #brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    product_type = db.Column(db.String(50), nullable=False)  # 'simple', 'variant', 'bundle'

    def to_dict_pro(self):
        return {
            'id': self.id,
            'parent_id': self.parent_id,
            'name': self.name,
            'description': self.description,
            'sku_id': self.sku_id,
            'barcode': self.barcode,
            'price': self.price,
            'vendor_id': self.vendor_id,
            #'brand_id': self.brand_id,
            'product_type': self.product_type
        }
    
class PriceType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'vendor_id': self.vendor_id

        }
class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    charges = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'value': self.value,
            'charges': self.charges
        }

class ProductPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    price_type_id = db.Column(db.Integer, db.ForeignKey('price_type.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'price_type_id': self.price_type_id,
            'price': self.price
        }
    
class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'vendor_id': self.vendor_id
        }   
    
class ProductTranslation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    textTitle = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'language_id': self.language_id,
            'textTitle': self.textTitle,
            'text': self.text,
            'description': self.description,
            'vendor_id': self.vendor_id
        }
    
class Brands(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'vendor_id': self.vendor_id
        }
    
class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'parent_id': self.parent_id if self.parent_id else None,
            'vendor_id': self.vendor_id
        }
    
class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'category_id': self.category_id
        }
class Distributor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_number = db.Column(db.Integer, unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'mobile_number': self.mobile_number,
            'address_id': self.address_id,
            'vendor_id': self.vendor_id
        }
    
class ProductDistributor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    distributor_id = db.Column(db.Integer, db.ForeignKey('distributor.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'distributor_id': self.distributor_id,
            'vendor_id': self.vendor_id
        }

class BrandDistributor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    distributor_id = db.Column(db.Integer, db.ForeignKey('distributor.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'brand_id': self.brand_id,
            'distributor_id': self.distributor_id
        }
    
class VendorDistributor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    distributor_id = db.Column(db.Integer, db.ForeignKey('distributor.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'vendor_id': self.vendor_id,
            'distributor_id': self.distributor_id
        }
    
class Hubs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    hub_type = db.Column(db.String(50), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('hubs.id'), nullable=True)

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
class HubProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hub_id = db.Column(db.Integer, db.ForeignKey('hubs.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False) 
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    min_req_quantity = db.Column(db.Integer, nullable=True)
    max_stock_quantity = db.Column(db.Integer, nullable=True)

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
    
#model for moving stock between hubs or purchasing from distributor
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
    
#model for tracing the movement of stock between hubs or from distributor to hub
class StockMovementTrace(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_movement_id = db.Column(db.Integer, db.ForeignKey('stock_movement.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'inititated', 'in_transit', 'delivered', 'cancelled'
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    contact_person = db.Column(db.String(100), nullable=True)
    contact_number = db.Column(db.String(20), nullable=True)
    remarks = db.Column(db.String(500), nullable=True)

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
    
class DistributorPaymentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    distributor_id = db.Column(db.Integer, db.ForeignKey('distributor.id'), nullable=False)
    stock_movement_ids = db.Column(db.String(500), nullable=True)  # Comma-separated IDs
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    payment_method = db.Column(db.String(50), nullable=False)  # 'bank_transfer', 'credit_card', etc.
    transaction_id = db.Column(db.String(100), nullable=True)
    remarks = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'distributor_id': self.distributor_id,
            'stock_movement_ids': self.stock_movement_ids,
            'amount': self.amount,
            'payment_date': self.payment_date,
            'payment_method': self.payment_method,
            'transaction_id': self.transaction_id,
            'remarks': self.remarks
        }
    
class CartModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'vendor_id': self.vendor_id
        }
    
#order and order items model for placing orders from the cart
class OrderModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    delivery_address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    hub_id = db.Column(db.Integer, db.ForeignKey('hubs.id'), nullable=True)
    status = db.Column(db.String(20), nullable=False)  # 'pending', 'confirmed', 'shipped', 'delivered', 'cancelled'
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    delivery_partner_id = db.Column(db.Integer, db.ForeignKey('delivery_partner_model.id'), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'total_amount': self.total_amount,
            'order_date': self.order_date,
            'status': self.status,
            'vendor_id': self.vendor_id,
            'delivery_partner_id': self.delivery_partner_id if self.delivery_address_id else None
        }
    
class OrderItemModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order_model.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': self.price
        }
    
class OrderTraceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order_model.id'), nullable=False)
    track_url = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(20), nullable=False)  # 'pending', 'confirmed', 'shipped', 'delivered', 'cancelled'
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    remarks = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'status': self.status,
            'timestamp': self.timestamp,
            'remarks': self.remarks
        }

class PaymentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order_model.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    payment_method = db.Column(db.String(50), nullable=False)  # 'bank_transfer', 'credit_card', etc.
    transaction_id = db.Column(db.String(100), nullable=True)
    remarks = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'amount': self.amount,
            'payment_date': self.payment_date,
            'payment_method': self.payment_method,
            'transaction_id': self.transaction_id,
            'remarks': self.remarks
        }

class DeliveryPartnerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_number = db.Column(db.Integer, unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    hub_id = db.Column(db.Integer, db.ForeignKey('hubs.id'), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'mobile_number': self.mobile_number,
            'address_id': self.address_id,
            'vendor_id': self.vendor_id
        }
    
class SEOSearchEngineModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    search_engine_name = db.Column(db.String(100), nullable=False)
    search_engine_url = db.Column(db.String(500), nullable=False)

#advanced seo data model for product pages to improve search engine ranking
class SEORankingModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=True)
    meta_title = db.Column(db.String(150), nullable=True)
    meta_description = db.Column(db.String(300), nullable=True)
    meta_keywords = db.Column(db.String(500), nullable=True)
    canonical_url = db.Column(db.String(500), nullable=True)
    robots_content = db.Column(db.String(100), nullable=True)  
    hreflang = db.Column(db.String(100), nullable=True)  
    schema_json = db.Column(db.Text, nullable=True)
    rich_snippet_enabled = db.Column(db.Boolean, nullable=False, default=False)
    og_title = db.Column(db.String(150), nullable=True)
    og_description = db.Column(db.String(300), nullable=True)
    og_image = db.Column(db.String(500), nullable=True)
    twitter_title = db.Column(db.String(150), nullable=True)
    twitter_description = db.Column(db.String(300), nullable=True)
    twitter_image = db.Column(db.String(500), nullable=True)
    page_load_time_ms = db.Column(db.Integer, nullable=True)
    readability_score = db.Column(db.Float, nullable=True)
    seo_score = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'vendor_id': self.vendor_id,
            'meta_title': self.meta_title,
            'meta_description': self.meta_description,
            'meta_keywords': self.meta_keywords,
            'canonical_url': self.canonical_url,
            'robots_content': self.robots_content,
            'hreflang': self.hreflang,
            'schema_json': self.schema_json,
            'rich_snippet_enabled': self.rich_snippet_enabled,
            'og_title': self.og_title,
            'og_description': self.og_description,
            'og_image': self.og_image,
            'twitter_title': self.twitter_title,
            'twitter_description': self.twitter_description,
            'twitter_image': self.twitter_image,
            'page_load_time_ms': self.page_load_time_ms,
            'readability_score': self.readability_score,
            'seo_score': self.seo_score,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
