# autonomous_agent.py

import datetime

def decompose_goal(goal):
    """
    Break a high-level goal into structured steps
    """
    goal = goal.lower()
    steps = []

    if "internship" in goal:
        steps = [
            "Build core skills",
            "Create 2-3 projects",
            "Build resume",
            "Create GitHub portfolio",
            "Apply for internships",
            "Prepare for interviews"
        ]

    elif "job" in goal:
        steps = [
            "Master required skills",
            "Build strong projects",
            "Create resume",
            "Optimize LinkedIn",
            "Apply for jobs",
            "Prepare interviews"
        ]

    elif "ai" in goal:
        steps = [
            "Learn Python deeply",
            "Learn ML basics",
            "Build ML projects",
            "Learn deep learning",
            "Deploy models",
            "Build AI portfolio"
        ]

    else:
        steps = [
            "Skill assessment",
            "Learning phase",
            "Practice phase",
            "Project phase",
            "Application phase"
        ]

    return steps


def generate_autonomous_plan(goal, missing_skills):
    """
    Build timeline + task plan
    """
    steps = decompose_goal(goal)
    plan = []

    week = 1
    for step in steps:
        task = f"Work on: {step}"

        if missing_skills:
            task += f" | Focus skills: {', '.join(missing_skills)}"

        plan.append({
            "week": week,
            "step": step,
            "task": task,
            "status": "pending"
        })
        week += 1

    return plan


def autonomous_reasoning(memory, current_score):
    """
    AI decision engine
    """
    decisions = []

    if current_score < 40:
        decisions.append("System Decision: Focus on learning, not applying.")
    elif current_score < 70:
        decisions.append("System Decision: Build projects before applying.")
    else:
        decisions.append("System Decision: Start applications and interviews.")

    if memory:
        decisions.append("System Decision: Use past memory to personalize strategy.")

    return decisions


def update_agent_state(memory, new_data):
    """
    Self-updating intelligence
    """
    state = memory if memory else {}
    timestamp = datetime.datetime.now().isoformat()

    state["last_update"] = timestamp
    state["last_action"] = new_data

    return state
