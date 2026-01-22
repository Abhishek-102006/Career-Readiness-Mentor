def find_missing_skills(user_skills, job_skills):
    missing_skills = []

    for skill in job_skills:
        if skill not in user_skills:
            missing_skills.append(skill)

    return missing_skills
