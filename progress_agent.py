# progress_agent.py

def track_progress(roadmap, completed_weeks):
    progress = []

    for item in roadmap:
        status = "completed" if item["week"] in completed_weeks else "pending"
        progress.append({
            "week": item["week"],
            "skill": item.get("skill", ""),
            "status": status
        })

    return progress
