# models.py
from db import db  # Import db instance to define models

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # tasks = db.relationship('Task', backref='user', lazy=True)

class Task(db.Model):
    __tablename__ = 'task'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    assignments = db.relationship('Assignment', backref='task', lazy=True)

class Assignment(db.Model):
    __tablename__ = 'assignment'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    start_index = db.Column(db.Integer)
    end_index = db.Column(db.Integer)
    date = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)

class Proofread(db.Model):
    __tablename__ = 'proofread'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    input = db.Column(db.String(255), nullable=False)
    expect = db.Column(db.String(255))
    expect_raw = db.Column(db.String(255))
    modifier_date = db.Column(db.String(50))
    duration_review = db.Column(db.Integer)
    ip_review = db.Column(db.String(50))
