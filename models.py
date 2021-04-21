import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_path = "postgres://mbiwdaadknzeib:b6049ba04911e612b4f9a5555e21b7468f2033b1e554c729bf2599f606827649@ec2-18-206-20-102.compute-1.amazonaws.com:5432/d84bo7akva22br"

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    migrate = Migrate(app, db)
    db.app = app
    db.init_app(app)
    db.create_all()
