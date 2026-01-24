import streamlit as st
DASHBOARD_MODE = st.toggle("🧭 Enable Dashboard Mode", value=True)
from skill_gap import find_missing_skills
from job_roles import JOB_ROLE_SKILLS
from jd_parser import extract_skills_from_jd
from roadmap import generate_roadmap
from readiness_score import calculate_readiness
from agent_memory import save_memory, load_memory
from ai_brain import generate_ai_recommendations
from career_chat import ai_chat_agent
from autonomous_agent import (
    decompose_goal,
    generate_autonomous_plan,
    autonomous_reasoning,
    update_agent_state
)
from learning_agent import adapt_strategy
from progress_agent import track_progress
from prediction_agent import predict_readiness_timeline
from skill_graph import get_skill_path


st.title("Career Readiness Mentor & Skill-Gap Navigator")

memory = load_memory()

st.write("Enter your skills and optionally paste a job description.")

user_input = st.text_input("Enter your skills (comma separated)")
role = st.selectbox("Select Target Job Role", JOB_ROLE_SKILLS.keys())
jd_text = st.text_area("Paste Job Description (optional)")

default_job_skills = JOB_ROLE_SKILLS[role]

if jd_text.strip():
    job_skills = extract_skills_from_jd(jd_text, default_job_skills)
else:
    job_skills = default_job_skills

if st.button("Check Skill Gap"):
    user_skills = [skill.strip() for skill in user_input.split(",")]

    if not job_skills:
        st.warning("No skills could be extracted from the job description.")

    else:
        missing_skills = find_missing_skills(user_skills, job_skills)

    # 👉 ADD SCORE HERE
    score = calculate_readiness(user_skills, job_skills)

    roadmap = generate_roadmap(missing_skills)

    # 🧠 Save agent memory
    save_memory({
            "user_skills": user_skills,
            "role": role,
            "job_skills": job_skills,
            "missing_skills": missing_skills,
            "score": score,
            "roadmap": roadmap
        })


    if DASHBOARD_MODE:

        # ====== ROW 1 ======
        col1, col2 = st.columns([1, 2])

        with col1:
                st.subheader("👤 Profile")
                st.write(f"**Target Role:** {role}")
                st.write(f"**Your Skills:** {', '.join(user_skills)}")
                st.write(f"**Required Skills:** {', '.join(job_skills)}")

        with col2:
                st.subheader("📊 Career Readiness Score")
                st.progress(int(score))
                st.write(f"Readiness Level: {score}%")

        st.divider()

        # ====== ROW 2 ======
        col3, col4 = st.columns(2)

        with col3:
                st.subheader("❌ Missing Skills")
                if missing_skills:
                    for skill in missing_skills:
                        st.write("❌", skill)
                else:
                    st.success("No missing skills 🎉")

        with col4:
                st.subheader("📍 Personalized Learning Roadmap")
                if missing_skills:
                    for item in roadmap:
                        st.write(
                            f"**Week {item['week']}** — {item['goal']}  \n"
                            f"👉 {item['task']}"
                        )
                else:
                    st.write("No roadmap needed")

        st.divider()

        # ====== ROW 3 ======
        st.subheader("🧠 Agent Memory (Persistent Intelligence)")
        memory = load_memory()
        if memory:
                st.json(memory)
        else:
                st.write("No memory stored yet.")

    else:
            st.subheader("📊 Career Readiness Score")
            st.progress(int(score))
            st.write(f"Readiness Level: {score}%")

            st.subheader("❌ Missing Skills")
            for skill in missing_skills:
                st.write("❌", skill)

            st.subheader("📍 Personalized Learning Roadmap")
            for item in roadmap:
                st.write(
                    f"Week {item['week']}: {item['goal']}  \n"
                    f"👉 Task: {item['task']}"
                )
                
    # 🤖 AI Career Agent Output
    st.subheader("🤖 AI Career Mentor Recommendations")

    ai_tips = generate_ai_recommendations(
        user_skills=user_skills,
        missing_skills=missing_skills,
        role=role,
        score=score
    )

    for tip in ai_tips:
        st.info(tip)

    st.divider()
    st.subheader("💬 AI Career Mentor Chat")

    user_msg = st.text_input("Ask your AI Mentor")

    if user_msg:
        memory = load_memory()
        reply = ai_chat_agent(user_msg, memory)
        st.chat_message("assistant").write(reply)

    # ============================
    # 🤖 AUTONOMOUS AI AGENT
    # ============================
    st.divider()
    st.subheader("🤖 Autonomous AI Career Agent")

    user_goal = st.text_input("🎯 Enter your career goal (e.g. 'Get internship in 3 months')")

    if user_goal:
        memory = load_memory()

        st.subheader("🧠 Goal Decomposition")
        steps = decompose_goal(user_goal)
        for i, step in enumerate(steps, 1):
            st.write(f"{i}. {step}")

        st.subheader("🗺 Autonomous Plan")
        plan = generate_autonomous_plan(user_goal, missing_skills)
        for item in plan:
            st.write(f"Week {item['week']} → {item['step']}")
            st.write(f"👉 Task: {item['task']}")
            st.write(f"📌 Status: {item['status']}")
            st.divider()

        st.subheader("🧠 Autonomous Reasoning Engine")
        decisions = autonomous_reasoning(memory, score)
        for d in decisions:
            st.warning(d)

        # Self-update memory
        updated_state = update_agent_state(memory, {
            "goal": user_goal,
            "plan": plan,
            "decisions": decisions
        })

        save_memory(updated_state)
   
    # ============================
    # 🧠 SELF-LEARNING AI AGENT
    # ============================
    st.divider()
    st.subheader("🧠 Self-Learning AI Agent")

    completed_weeks = st.multiselect(
        "✅ Select completed weeks from roadmap",
        options=[item["week"] for item in roadmap]
    )

    progress_data = {
        "completed_tasks": len(completed_weeks)
    }

    # 📈 Progress tracking
    progress_state = track_progress(roadmap, completed_weeks)
    st.subheader("📈 Progress Tracker")
    for p in progress_state:
        st.write(f"Week {p['week']} → {p['status']}")

    # 🧠 Adaptive learning
    memory = load_memory()
    adaptation = adapt_strategy(memory, progress_data)

    st.subheader("🧠 Adaptive Intelligence")
    for a in adaptation:
        st.info(a)

    # 🔮 Prediction engine
    progress_rate = "fast" if len(completed_weeks) > 2 else "slow"
    prediction = predict_readiness_timeline(score, progress_rate)

    st.subheader("🔮 AI Prediction Engine")
    st.success(prediction)

    # 🧩 Skill dependency graph
    st.subheader("🧩 Skill Growth Path")
    for skill in missing_skills:
        path = get_skill_path(skill)
        st.write(f"{skill} → {' → '.join(path)}")
