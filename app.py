from flask import Flask
from extension import db

from routes.distributor import Distributor_bp
from routes.order import OrderModel_bp
from routes.payment import PaymentModel_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/it_fixtures'
db.init_app(app)

app.register_blueprint(Distributor_bp)
app.register_blueprint(OrderModel_bp)
app.register_blueprint(PaymentModel_bp)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
