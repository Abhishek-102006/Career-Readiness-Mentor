# ai_brain.py

def generate_ai_recommendations(user_skills, missing_skills, role, score):
    tips = []

    # Strategy-based recommendations
    if score < 40:
        tips.append("📉 Your readiness is low. Focus on fundamentals and consistency before advanced topics.")
    elif score < 70:
        tips.append("📈 You are on the right track. Start building real-world projects alongside learning.")
    else:
        tips.append("🚀 You are job-ready. Start applying for internships/jobs and polishing your portfolio.")

    # Skill-based recommendations
    if "Data Structures" in missing_skills:
        tips.append("🧠 Priority: Learn Data Structures (arrays, stacks, queues, linked lists, trees).")

    if "Algorithms" in missing_skills:
        tips.append("⚙️ Priority: Learn Algorithms (searching, sorting, recursion, DP basics).")

    if "SQL" in missing_skills:
        tips.append("🗄️ Priority: Learn SQL for backend, analytics, and interviews.")

    # Role-based intelligence
    if role == "Software Engineer":
        tips.append("💼 Focus on DSA + GitHub projects + system basics.")
    elif role == "Data Scientist":
        tips.append("📊 Focus on Python, ML basics, statistics, and real datasets.")
    elif role == "AI Engineer":
        tips.append("🤖 Focus on ML, DL, model training, and deployment skills.")

    # Learning strategy
    tips.append("📅 Daily rule: 2 hrs learning + 1 hr practice + 30 min revision.")
    tips.append("🧩 Build 1 mini-project per missing skill.")
    tips.append("📁 Maintain a learning portfolio on GitHub.")

    return tips
