# skill_graph.py

SKILL_GRAPH = {
    "Python": ["Data Structures"],
    "Data Structures": ["Algorithms"],
    "Algorithms": ["Problem Solving"],
    "Problem Solving": ["Interviews"],
    "SQL": ["Backend"],
    "Backend": ["System Design"],
    "System Design": ["Job Ready"]
}

def get_skill_path(start_skill):
    path = []
    current = start_skill

    while current in SKILL_GRAPH:
        next_skill = SKILL_GRAPH[current][0]
        path.append(next_skill)
        current = next_skill

    return path
