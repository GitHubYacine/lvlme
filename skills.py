from app import app, Skills, db

sample_skills = [
        {"name": "Strength", "level": 1},
        {"name": "Defence", "level": 1},
        {"name": "Prayer", "level": 1},
        {"name": "Construction", "level": 1},
        {"name": "Heart", "level": 1},
        {"name": "Agility", "level": 1},
        {"name": "Farming", "level": 1},
        {"name": "Gaming", "level": 1},
        {"name": "Knowledge", "level": 1},
        {"name": "Cooking", "level": 1},
        {"name": "Creativity", "level": 1},
        {"name": "Coding", "level": 1},
    ]

with app.app_context():
    for skill_data in sample_skills:
        skills = Skills(name=skill_data["name"], level=skill_data["level"])
        db.session.add(skills)
    db.session.commit()