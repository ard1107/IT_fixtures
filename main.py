from flask import Flask,request,jsonify 
from extension import db  
from datetime import datetime
   
from routes.deliveryPartnerModel import DeliveryPartnerModel
from routes. import SEOSearchEngineModel 
from routes.seoranking import SEORankingModel



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1712@localhost/IT_fixtures'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 

db.init_app(app)

app.register_blueprint(delivery_bp )
app.register_blueprint(seosearch_bp)
app.register_blueprint(seoranking_bp ) 

@app.route('/')
def home():
    return "home page"


if __name__=="__main__":
    with app.app_context():
        db.create_all() 
app.run(debug=True)  