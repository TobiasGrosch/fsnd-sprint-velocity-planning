import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "postgresql-reticulated-70328"
database_path = "postgresql://postgres:postgres@localhost:5432/{}".format(database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
