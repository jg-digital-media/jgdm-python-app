 # Declare imports for the app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


# Connect to SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///roster.db'

app.secret_key = "gggd465dfgghffhehshy"  # Secret key


db = SQLAlchemy(app)


# Create Database Model - 3 fields + ID as primary key
class Roster(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column("Name", db.String(80), unique=True, nullable=False)
    age = db.Column("Age", db.Integer, unique=True, nullable=False)
    description = db.Column("Description", db.String(280), unique=True, nullable=False)
    joined = db.Column('Joined', db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'''<Roster %r> ({self.name} 
        Age: {self.age}
        Joined: {self.joined }
       '''