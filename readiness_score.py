def calculate_readiness(user_skills, job_skills):
    matched = 0

    for skill in job_skills:
        if skill in user_skills:
            matched += 1

    if len(job_skills) == 0:
        return 0

    score = (matched / len(job_skills)) * 100
    return round(score, 2)
