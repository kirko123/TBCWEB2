from ext import app, db
from models import Info, User, Question , Answer
from datetime import datetime

with app.app_context():
    db.create_all()

    admin_user = User("admin", "admin123", datetime(2024, 6, 5), "Admin")
    info1 = Info("Python", "Python is a versatile programming language known for its simplicity and readability.")
    info2 = Info("JavaScript", "JavaScript is a programming language that enables interactive web pages and web applications.")
    info3 = Info("Java", "Java is a widely-used programming language for building enterprise-scale applications.")
    info4 = Info("C++", "C++ is a powerful programming language used for system/application software, game development, drivers, and more.")
    info5 = Info("Python", "Python is a versatile programming language known for its simplicity and readability.")
    info6 = Info("JavaScript", "JavaScript is a programming language that enables interactive web pages and web applications.")

    db.session.add(admin_user)
    db.session.add(info1)
    db.session.add(info2)
    db.session.add(info3)
    db.session.add(info4)
    db.session.add(info5)
    db.session.add(info6)
    db.session.commit()













    








 
