import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask import Flask,render_template
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
db = SQLAlchemy(app)
@app.route('/')
def landing():
    return render_template('index.html')
from routes.authroutes import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')
if __name__ == '__main__':   
    app.run(debug=True)
