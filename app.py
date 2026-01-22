import streamlit as st
DASHBOARD_MODE = st.toggle("🧭 Enable Dashboard Mode", value=True)
from skill_gap import find_missing_skills
from job_roles import JOB_ROLE_SKILLS
from jd_parser import extract_skills_from_jd
from roadmap import generate_roadmap
from readiness_score import calculate_readiness
from agent_memory import save_memory, load_memory

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
