from flask import Blueprint, Flask, jsonify, request, render_template, redirect, url_for
from models.db_models import Skill, Challenge, Roadmap
from routes.utilities import update_experience
from models.database import db

user_bp = Blueprint("User", __name__)

@user_bp.route('/')
def first_page():
    skills = Skill.query.all()
    for skill in skills:
        skill.required_experience = 100 * pow(1.1, skill.level-1)
        skill.required_experience = round(skill.required_experience, 2)
    return render_template("user/user_dashboard.html", skills=skills, totalLevel=sum(skill.level for skill in skills))
    
@user_bp.route('/skills', methods=['GET'])
def get_skills():
    skills = Skill.query.all()
    return jsonify([{'name': skill.name, 'level': skill.level} for skill in skills])

@user_bp.route('/update_skill_up', methods=['POST'])
def update_skill_up():
    data = request.form
    skill = Skill.query.filter_by(name=data['skill']).first()
    if skill:
        skill.level += 1
        db.session.commit()
    skills = Skill.query.all()
    return redirect(url_for('User.first_page'))

@user_bp.route('/update_skill_down', methods=['POST'])
def update_skill_down():
    data = request.form
    skill = Skill.query.filter_by(name=data['skill']).first()
    if skill and skill.level > 1:
        skill.level -= 1
        db.session.commit()
    skills = Skill.query.all()
    return redirect(url_for('User.first_page'))

@user_bp.route('/update_experience/<int:skill_id>', methods=['POST'])
def update_experience_route(skill_id):
    minutes_spent = request.form.get('minutes_spent')
    if minutes_spent.isdigit():
        update_experience(skill_id, int(minutes_spent))
        return redirect(url_for('User.first_page'))
    else:
        return "Please enter a valid number for minutes spent"
    
@user_bp.route('/complete_challenge/<int:challenge_id>', methods=['POST'])
def complete_challenge(challenge_id):
    completed = request.form.get('completed') == 'true'
    challenge = Challenge.query.get(challenge_id)
    if challenge and completed:
        update_experience(challenge_id)
    return redirect(url_for('User.first_page'))

@user_bp.route('/show_roadmap/<int:skill_id>', methods=['GET'])
def show_roadmap(skill_id):
    skill = Skill.query.get(skill_id)
    if skill:
        challenges = skill.challenges
        if challenges:
            return render_template("user/user_roadmap.html", challenges=challenges, skill=skill)
        else:
            return "No roadmap found for this skill, you need to create a roadmap for said skill Yacine, do not panic.", 404
    else:
        return "No skill was found", 404