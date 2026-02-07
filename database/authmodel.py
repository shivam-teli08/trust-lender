from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(100))
    age = db.Column(db.Intger,default=18,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone = db.Column(db.String(20), unique=True, nullable=True)
    age = db.Column(db.Integer, default=18, nullable=False)
    auth_provider = db.Column(db.String(50), nullable=False)
    auth_id = db.Column(db.String(200), unique=True, nullable=False)
    trust_score = db.Column(db.Float, default=5.0)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp()) 