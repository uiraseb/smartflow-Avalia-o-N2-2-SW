# app/models.py
from .extensions import db
from datetime import datetime

class Workflow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class WorkflowStep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workflow_id = db.Column(db.Integer, db.ForeignKey('workflow.id'))
    step_name = db.Column(db.String(100))
    result = db.Column(db.Text)
    status = db.Column(db.String(50), default='pending')