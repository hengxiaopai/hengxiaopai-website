import argparse
from pathlib import Path

from .models import Project
from .scoring import score_project
from .templates import ARTICLE_TEMPLATE, VIDEO_SCRIPT_TEMPLATE


DEMO_PROJECT = Project(
    name="GitHub Hot Article Studio",
    url="https://github.com/hengxiaopai/hengxiaopai-website",
    description="自动发现 GitHub 热点项目，并生成微信公众号文章、封面提示词和视频脚本。",
    stars=860,
    forks=96,
    language="Python",
    topics=["github", "wechat", "ai", "content", "automation"],
    readme_summary="A content production pipeline for GitHub trending projects.",
    article_angle="它把 GitHub 项目发现、内容策划、中文长文生成和视频脚本生成串成了一条自动化流水线。",
)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run_demo() -> None:
    project = DEMO_PROJECT
    project.hot_score = score_project(project)

    article = ARTICLE_TEMPLATE.format(
        title="这个开源项目，想把 GitHub 热点自动变成公众号文章",
        name=project.name,
        url=project.url,
        description=project.description,
        stars=project.stars,
        forks=project.forks,
        language=project.language,
        hot_score=project.hot_score,
        angle=project.article_angle,
    )

    cover_prompt = """公众号封面图，主题是 GitHub 热点项目自动生成微信公众号文章。画面包含 GitHub 星标、代码窗口、中文公众号文章卡片、AI 自动化流水线。风格为玻璃质感、蓝青色全息光、白色极简科技背景，高级、清爽、适合科技公司公众号。"""

    write_text(Path("outputs/articles/demo-article.md"), article)
    write_text(Path("outputs/covers/demo-cover-prompt.txt"), cover_prompt)
    write_text(Path("outputs/videos/demo-video-script.md"), VIDEO_SCRIPT_TEMPLATE)

    print("Demo outputs generated under outputs/.")


def main() -> None:
    parser = argparse.ArgumentParser(description="GitHub Hot Article Studio")
    parser.add_argument("--mode", default="demo", choices=["demo"], help="Run mode")
    args = parser.parse_args()

    if args.mode == "demo":
        run_demo()


if __name__ == "__main__":
    main()
