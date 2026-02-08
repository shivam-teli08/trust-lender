from database.authmodel import Trust_lender_users as User
from app import app, db
from werkzeug.security import generate_password_hash

with app.app_context():

    # Create tables first (if not exists)
    db.create_all()
    print("✅ Tables created/updated successfully")

    for i in range(1, 10):

        normal_password = f"password{i}"

        user = User(
            name=f"User {i}",
            email=f"user{i}@example.com",
            phone=f"123456789{i}",
            age=20 + i,
            auth_provider='local',
            password=generate_password_hash(normal_password)
        )

        db.session.add(user)

        # Save plain data to txt file (optional)
        with open(f"user{i}_data.txt", "w") as f:
            f.write(f"Name: User {i}\n")
            f.write(f"Email: user{i}@example.com\n")
            f.write(f"Phone: 123456789{i}\n")
            f.write(f"Age: {20 + i}\n")
            f.write(f"Auth Provider: local\n")
            f.write(f"Password: {normal_password}\n")

    # Commit once after loop (BEST PRACTICE)
    db.session.commit()

    print("✅ Bulk insert completed successfully")

    db.session.close()
