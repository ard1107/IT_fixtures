from flask import Flask
from models import db,init_db
from routes.Users import Users_blueprint
from routes.Vendors import Vendors_blueprint
from routes.Address import Address_blueprint
from routes.MediaFiles import MediaFiles_blueprint
from routes.Product import Product_blueprint

# OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:Mysql123@localhost/fix"
init_db(app)

# ---- OpenTelemetry Setup ----
trace.set_tracer_provider(TracerProvider())


span_processor = BatchSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

FlaskInstrumentor().instrument_app(app)

# ---- Register Blueprint ----
app.register_blueprint(Users_blueprint)

app.register_blueprint(Address_blueprint)

app.register_blueprint(Vendors_blueprint)

app.register_blueprint(MediaFiles_blueprint)

app.register_blueprint(Product_blueprint)
   
     


@app.route("/")
def home():
    return "Welcome Ecommerce"

if __name__ == "__main__":
    app.run(debug=False)