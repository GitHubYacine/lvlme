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


