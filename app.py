from flask import Flask,request, jsonify
from models import *
from datetime import datetime
from routes.OrderItemModel import OrderItemModel_bp
from routes.OrderTraceModel import OrderTraceModel_bp
from routes.PaymentModel import PaymentModel_bp


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1712ad@localhost/it_fixtures'
db.init_app(app)

app.register_blueprint(OrderItemModel_bp)
app.register_blueprint(OrderTraceModel_bp)
app.register_blueprint(PaymentModel_bp)

@app.route('/')
def home():
    return "Welcome to the IT Fixtures API" 


if __name__=="__main__":
    with app.app_context():
        db.create_all()
app.run(debug=True)