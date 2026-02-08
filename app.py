import os
from flask import Flask, render_template
from dotenv import load_dotenv
from extensions import db

load_dotenv()

app = Flask(__name__)

# Secret key
app.secret_key = os.getenv("SECRET_KEY")

# PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

# Recommended settings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
    "pool_recycle": 300,
}

# Initialize database
db.init_app(app)


# Import models AFTER db init (important)
from database.authmodel import Trust_lender_users   # make sure User model exists


# Create tables automatically
with app.app_context():
    db.create_all()


# Routes
@app.route('/')
def landing():
    return render_template('index.html')


# Register blueprint
from routes.authroutes import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')


# Run app
if __name__ == '__main__':
    app.run(debug=True)
