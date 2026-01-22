def extract_skills_from_jd(jd_text, known_skills):
    jd_text = jd_text.lower()
    extracted_skills = []

    for skill in known_skills:
        if skill.lower() in jd_text:
            extracted_skills.append(skill)

    return extracted_skills
