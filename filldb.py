from app import app, db, Challenge
from models.db_models import Skill

sample_skills = [
        {"name": "Strength", "level": 1, "experience": 0, "description": "Strength represents your physical power.", "skill_image": ""},
        {"name": "Defence", "level": 1, "experience": 0, "description": "Defence represents your ability to protect yourself either by fighting or discussing.", "skill_image": ""},
        {"name": "Prayer", "level": 1, "experience": 0, "description": "Prayer represents your practice of communicating with a higher power seeking guidance, blessings, or inner peace.", "skill_image": ""},
        {"name": "Construction", "level": 1, "experience": 0, "description": "Construction represents the art and science of building structures and infrastructures.", "skill_image": ""},
        {"name": "Heart", "level": 1, "experience": 0, "description": "Heart represents your cardiovascular endurance and the efficiency of your circulatory system during physical activities.", "skill_image": ""},
        {"name": "Agility", "level": 1, "experience": 0, "description": "Agility represents your ability to move quickly and easily, showcasing physical dexterity or adaptability.", "skill_image": ""},
        {"name": "Farming", "level": 1, "experience": 0, "description": "Farming represents the cultivation of plants and rearing of animals to produce food and other products.", "skill_image": ""},
        {"name": "Gaming", "level": 1, "experience": 0, "description": "Gaming represents the act of playing games, ranging from video games to board games.", "skill_image": ""},
        {"name": "Knowledge", "level": 1, "experience": 0, "description": "Knowledge represents the accumulation of facts, information, and skills acquired through experience or education.", "skill_image": ""},
        {"name": "Cooking", "level": 1, "experience": 0, "description": "Cooking represents the art and technique of preparing food by combining and heating ingredients.", "skill_image": ""},
        {"name": "Creativity", "level": 1, "experience": 0, "description": "Creativity represents the ability to produce original and imaginative ideas or art.", "skill_image": ""},
        {"name": "Coding", "level": 1, "experience": 0, "description": "Coding represents the practice of writing computer programs using programming languages.", "skill_image": ""},
    ]

challenges_for_skills = [
    {"name": "Challenge 1 for Strength", "description": "Do a push-up.", "requiredLevel": 10, "skill_id": 1},
    {"name": "Challenge 2 for Strength", "description": "Do a squat.", "requiredLevel": 20, "skill_id": 1},
    {"name": "Challenge 3 for Strength", "description": "Do a sit-up.", "requiredLevel": 30, "skill_id": 1},
    {"name": "Challenge 4 for Strength", "description": "Do a push-up.", "requiredLevel": 40, "skill_id": 1},
    {"name": "Challenge 5 for Strength", "description": "Do a squat.", "requiredLevel": 50, "skill_id": 1},
    {"name": "Challenge 6 for Strength", "description": "Do a sit-up.", "requiredLevel": 60, "skill_id": 1},
    {"name": "Challenge 7 for Strength", "description": "Do a push-up.", "requiredLevel": 70, "skill_id": 1},
    {"name": "Challenge 8 for Strength", "description": "Do a squat.", "requiredLevel": 80, "skill_id": 1},
    {"name": "Challenge 9 for Strength", "description": "Do a sit-up.", "requiredLevel": 90, "skill_id": 1},  
]


with app.app_context():
    db.create_all()
    if True == True:
        for skill_data in sample_skills:
                skills = Skill(name=skill_data["name"], level=skill_data["level"], experience=skill_data["experience"], description=skill_data["description"], skill_image=skill_data["skill_image"])
                db.session.add(skills)
    if True == True:
        for challenge in challenges_for_skills:
            challenges = Challenge(name=challenge["name"], description=challenge["description"], requiredLevel=challenge["requiredLevel"], skill_id=challenge["skill_id"])
            db.session.add(challenges)
    db.session.commit()