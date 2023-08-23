from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skills.db'
db = SQLAlchemy(app)


@app.route('/')
def first_page():
    skills = Skills.query.all()
    return render_template("front.html", skills=skills)

@app.route('/skills', methods=['GET'])
def get_skills():
    skills = Skills.query.all()
    return jsonify([{'name': skill.name, 'level': skill.level} for skill in skills])

@app.route('/update_skill_up', methods=['POST'])
def update_skill_up():
    data = request.form
    skill = Skills.query.filter_by(name=data['skill']).first()
    if skill:
        skill.level += 1
        db.session.commit()
    skills = Skills.query.all()
    return render_template("front.html", skills=skills)

@app.route('/update_skill_down', methods=['POST'])
def update_skill_down():
    data = request.form
    skill = Skills.query.filter_by(name=data['skill']).first()
    if skill and skill.level > 1:
        skill.level -= 1
        db.session.commit()
    skills = Skills.query.all()
    return render_template("front.html", skills=skills)

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=True)


if __name__ == '__main__':
    app.run(debug=True)
    