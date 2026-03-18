from flask import Flask,request,jsonify
from models import db,init_db
from routes.Users import Users_blueprint
from routes.Vendors import Vendors_blueprint
from routes.Address import Address_blueprint
from routes.MediaFiles import MediaFiles_blueprint
from routes.Product import Product_blueprint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:Mysql123@localhost/IT_fixtures"
init_db(app)

app.register_blueprint(Users_blueprint)

app.register_blueprint(Vendors_blueprint)
   
app.register_blueprint(Address_blueprint)      


app.register_blueprint(MediaFiles_blueprint)


app.register_blueprint(Product_blueprint)    


@app.route("/")
def home():
    return "Welcome Ecommerce"
  
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=8000,debug=False)