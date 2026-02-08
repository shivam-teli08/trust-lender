from app import app, db
from database.authmodel import User   # make sure Transfer model exists
with app.app_context():
	db.create_all()
	print("✅ Tables created/updated successfully")