import os
from sqlalchemy import Column, String, Integer, create_engine, CheckConstraint
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

# works with heroku online db:  database_path = "postgresql://mbiwdaadknzeib:b6049ba04911e612b4f9a5555e21b7468f2033b1e554c729bf2599f606827649@ec2-18-206-20-102.compute-1.amazonaws.com:5432/d84bo7akva22br"

#database for local development:

database_name = "velocity"
database_path = "postgresql://postgres:postgres@localhost:5432/{}".format(database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    migrate = Migrate(app, db)
    db.app = app
    db.init_app(app)
    db.create_all()

class Developer(db.Model):
    __tablename__ = 'developers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    proj_participation = db.Column(db.Float, db.CheckConstraint('proj_participation <= 1')) #, proj_participation >= 0
    Vacation = db.relationship('Vacation', backref='parent', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def json_representation(self):
        return {
            'id': self.id,
            'name': self.name,
            'proj_participation': self.proj_participation
        }

class Sprint(db.Model):
    __tablename__ = 'sprints'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    sp_planned = db.Column(db.Integer)
    sp_finished = db.Column(db.Integer)
    velocity_factor = db.Column(db.Float)
    sprint_fte_sum = db.Column(db.Float)
    date_start = db.Column(db.DateTime)
    date_end = db.Column(db.DateTime)
    sp_predicitions_next_sprint = db.Column(db.Float)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def json_representation(self):
        return {
            'id':self.id,
            'name': self.name,
            'sp_planned': self.sp_planned,
            'sp_finished': self.sp_finished,
            'velocity_factor': self.velocity_factor,
            'sp_prediction_next_sprint': self.sp_predicitions_next_sprint,
            'sprint_fte_sum': self.sprint_fte_sum,
            'date_start': self.date_start,
            'date_end': self.date_end
        }

class Vacation(db.Model):
    __tablename__ = 'vacations'

    id = db.Column(db.Integer, primary_key=True)
    developer_id = db.Column(db.Integer, db.ForeignKey('developers.id'), nullable=False)
    date_start = db.Column(db.DateTime, nullable=False)
    date_end = db.Column(db.DateTime, nullable=False)
