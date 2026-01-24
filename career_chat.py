# career_chat.py

def ai_chat_agent(message, memory):
    msg = message.lower()
    response = ""

    if "job" in msg or "apply" in msg:
        response = "🚀 Start applying when your readiness score is above 70%. Build 2–3 solid projects before applying."

    elif "project" in msg:
        response = "🧩 Build projects aligned with missing skills. Example: SQL → student DB system, DSA → problem solver app."

    elif "learn" in msg or "study" in msg:
        response = "📚 Focus on fundamentals + practice. Follow roadmap strictly week by week."

    elif "internship" in msg:
        response = "🎯 Internships need skills + proof. Build GitHub projects and portfolio first."

    elif "time" in msg or "schedule" in msg:
        response = "⏱️ Daily plan: 2 hrs learning, 1 hr practice, 30 min revision."

    elif "career" in msg:
        response = "🧠 Your career path should be skill-driven, not degree-driven. Build skills + projects + proof."

    else:
        response = "🤖 I am your AI Career Mentor. Ask about learning paths, jobs, skills, projects, internships, or planning."

    return response
