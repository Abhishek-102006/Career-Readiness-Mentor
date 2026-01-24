# prediction_agent.py

def predict_readiness_timeline(score, progress_rate):
    if score < 40:
        months = 6
    elif score < 70:
        months = 3
    else:
        months = 1

    if progress_rate == "slow":
        months += 2
    elif progress_rate == "fast":
        months -= 1

    return f"Predicted job-readiness timeline: {months} month(s)"
