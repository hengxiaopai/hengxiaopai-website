from .models import Project


def score_project(project: Project) -> float:
    """Simple starter scoring model.

    The score is intentionally transparent so creators can adjust it.
    """
    star_score = min(project.stars / 1000, 10) * 4
    fork_score = min(project.forks / 200, 10) * 1.5
    topic_score = min(len(project.topics), 8) * 0.8
    readme_score = 8 if len(project.readme_summary) > 120 else 4
    demo_bonus = 5 if any(t in project.description.lower() for t in ["demo", "video", "agent", "app"]) else 0
    return round(star_score + fork_score + topic_score + readme_score + demo_bonus, 2)
