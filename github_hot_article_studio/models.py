from dataclasses import dataclass, field


@dataclass
class Project:
    name: str
    url: str
    description: str
    stars: int
    forks: int
    language: str
    topics: list[str] = field(default_factory=list)
    last_push: str = ""
    readme_summary: str = ""
    hot_score: float = 0.0
    article_angle: str = ""
