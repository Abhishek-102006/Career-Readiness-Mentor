def generate_roadmap(missing_skills):
    roadmap = []
    week = 1

    for skill in missing_skills:
        roadmap.append({
            "week": week,
            "skill": skill,
            "goal": f"Learn basics of {skill}",
            "task": f"Complete one beginner course and one mini-project on {skill}"
        })
        week += 1

    return roadmap
