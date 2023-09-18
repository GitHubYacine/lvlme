from models.database import db

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.Float, default=0)
    description = db.Column(db.String(500), nullable=True)
    challenges = db.relationship('Challenge', backref='skill', lazy=True)
    skill_image = db.Column(db.String(255), nullable=True)
    roadmap = db.relationship('Roadmap', backref='skill', lazy=True)

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    requiredLevel = db.Column(db.Integer(100), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"), nullable=False)

class Roadmap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    road = db.Column(db.String(500))
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"), nullable=False)