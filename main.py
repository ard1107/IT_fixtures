from flask import Flask,request,jsonify
from models import db,init_db
from routes.VendorDistributor import vendor_distributor_bp
from routes.Vendors import vendors_bp
from routes.Distributor import distributor_bp
#from routes.Hubs import Hubs_bp
#from routes.StockMovement import StockMovement_bp
#from routes.StockMovementTrace import StockMovementTrace_bp
#from routes.HubProduct import HubProduct_bp
#from routes.Address import Address_bp
#from flask_migrate import Migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ard11@localhost/IT_fixtures'
init_db(app)

app.register_blueprint(distributor_bp)
app.register_blueprint(vendor_distributor_bp)
app.register_blueprint(vendors_bp)
#app.register_blueprint(StockMovement_bp)
#app.register_blueprint(Hubs_bp)
#app.register_blueprint(HubProduct_bp)
#app.register_blueprint(Address_bp)
#app.register_blueprint(StockMovementTrace_bp)


with app.app_context():
    db.create_all()


if __name__ == '__main__':

    app.run(debug=True)


