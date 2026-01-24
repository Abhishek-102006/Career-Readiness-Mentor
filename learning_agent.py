# learning_agent.py

def adapt_strategy(memory, progress_data):
    updates = []

    if not memory:
        return ["No memory found. Starting fresh learning strategy."]

    completed = progress_data.get("completed_tasks", 0)

    if completed < 3:
        updates.append("AI Adaptation: Reduce complexity, focus on basics.")
    elif completed < 7:
        updates.append("AI Adaptation: Increase practice difficulty.")
    else:
        updates.append("AI Adaptation: Move to advanced projects.")

    updates.append("AI Adaptation: Adjust roadmap dynamically.")

    return updates
