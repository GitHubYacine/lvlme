from models.db_models import Skill
from models.database import db


def update_experience(skill_id, minutes_spent):
    skill = Skill.query.get(skill_id)
    skill_level_multiplier = 1.0 
    current_skill_level = skill.level
    experience_points = minutes_spent
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