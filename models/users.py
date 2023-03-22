from flask_sqlalchemy import SQLAlchemy
from models.enums import RoleType
from flask_migrate import Migrate
from app import db


#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(
        db.Enum(RoleType),
        default = RoleType.complainer,
        nullable=False,
    )
    iban = db.Column(db.String(22), )