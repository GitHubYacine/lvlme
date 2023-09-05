from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skills.db'
db = SQLAlchemy(app)

@app.route('/')
def first_page():
    skills = Skill.query.all()
    for skill in skills:
        skill.required_experience = 100 * pow(1.1, skill.level-1)
        skill.required_experience = round(skill.required_experience, 2)
    return render_template("front.html", skills=skills, totalLevel=sum(skill.level for skill in skills))
    
@app.route('/skills', methods=['GET'])
def get_skills():
    skills = Skill.query.all()
    return jsonify([{'name': skill.name, 'level': skill.level} for skill in skills])

@app.route('/update_skill_up', methods=['POST'])
def update_skill_up():
    data = request.form
    skill = Skill.query.filter_by(name=data['skill']).first()
    if skill:
        skill.level += 1
        db.session.commit()
    skills = Skill.query.all()
    return redirect(url_for('first_page'))

@app.route('/update_skill_down', methods=['POST'])
def update_skill_down():
    data = request.form
    skill = Skill.query.filter_by(name=data['skill']).first()
    if skill and skill.level > 1:
        skill.level -= 1
        db.session.commit()
    skills = Skill.query.all()
    return redirect(url_for('first_page'))

@app.route('/update_experience/<int:skill_id>', methods=['POST'])
def update_experience_route(skill_id):
    minutes_spent = request.form.get('minutes_spent')
    if minutes_spent.isdigit():
        update_experience(skill_id, int(minutes_spent))
        return redirect(url_for('first_page'))
    else:
        return "Please enter a valid number for minutes spent"
    
@app.route('/complete_challenge/<int:challenge_id>', methods=['POST'])
def complete_challenge(challenge_id):
    completed = request.form.get('completed') == 'true'
    challenge = Challenge.query.get(challenge_id)
    if challenge and completed:
        update_experience(challenge_id)
    return redirect(url_for('first_page'))

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.Float, default=0)
    description = db.Column(db.String(500), nullable=True)
    challenges = db.relationship('Challenge', backref='skill', lazy=True)
        
class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    experience = db.Column(db.Float(100), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"), nullable=False)


def update_experience(skill_id, minutes_spent):
    skill = Skill.query.get(skill_id)
    skill_level_multiplier = 1.0 
    current_skill_level = skill.level
    experience_points = ((minutes_spent) * (skill_level_multiplier * current_skill_level))
    corresponding_skill = skill
    int_experience_points = experience_points
    corresponding_skill.experience += int(experience_points)
    base_experience = 100
    newexperience = base_experience * pow(1.1, corresponding_skill.level-1)
    newexperience = round(newexperience, 2)
    if corresponding_skill.experience >= newexperience:
        corresponding_skill.level += 1
        corresponding_skill.experience -= newexperience
    db.session.commit()
    



if __name__ == '__main__':
    with app.app_context(): db.create_all()
    app.run(debug=True)