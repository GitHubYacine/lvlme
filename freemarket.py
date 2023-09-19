# def update_experience(challenge_id):
#     challenge = Challenge.query.get(challenge_id)
#     experience_points = challenge.experience
#     corresponding_skill = challenge.skill
#     corresponding_skill.experience += int(experience_points)
#     base_experience = 100
#     newexperience = base_experience * pow(1.1, corresponding_skill.level-1)
#     newexperience = round(newexperience, 2)
#     if corresponding_skill.experience >= newexperience:
#         corresponding_skill.level += 1
#         corresponding_skill.experience -= newexperience
#     db.session.commit()


# class Roadmap(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     road = db.Column(db.String(500))
#     tip_message = db.Column(db.String(500))
#     skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"), nullable=False)


# roadmap_for_skills = [
# {"road": "First step in Strength", "target_level": 1, "challenge_id": 1, "skill_id": 1},
# {"road": "Second step in Strength", "target_level": 2, "challenge_id": 2, "skill_id": 1},
# {"road": "Third step in Strength", "target_level": 3, "challenge_id": 1, "skill_id": 1},
# {"road": "Fourth step in Strength", "target_level": 4, "challenge_id": 2, "skill_id": 1},
# {"road": "Fifth step in Strength", "target_level": 5, "challenge_id": 1, "skill_id": 1},
# {"road": "Sixth step in Strength", "target_level": 6, "challenge_id": 2, "skill_id": 1},
# {"road": "Seventh step in Strength", "target_level": 7, "challenge_id": 1, "skill_id": 1},
# {"road": "Eigth step in Strength", "target_level": 8, "challenge_id": 2, "skill_id": 1},
# {"road": "Ninth step in Strength", "target_level": 9, "challenge_id": 1, "skill_id": 1},
# {"road": "Tenth step in Strength", "target_level": 10, "challenge_id": 2, "skill_id": 1},
# {"road": "Eleventh step in Strength", "target_level": 11, "challenge_id": 1, "skill_id": 1},
# {"road": "Twelfth step in Strength", "target_level": 12, "challenge_id": 2, "skill_id": 1},
# {"road": "Seventhyone step in Strength", "target_level": 72, "challenge_id": 2, }

    # if True == True:
    #     for roadmap_data in roadmap_for_skills:
    #         roadmap = Roadmap(road=roadmap_data["road"], skill_id=roadmap_data["skill_id"])
    #         db.session.add(roadmap)