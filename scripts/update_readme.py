from pathlib import Path
from collections import Counter
from datetime import datetime
import re


ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

PROBLEM_PATTERN = re.compile(r"^(\d+)-(.+)$")


def get_difficulty(folder):
    """Detect LeetCode difficulty from the problem README."""

    problem_readme = folder / "README.md"

    if not problem_readme.exists():
        return "Unknown"

    content = problem_readme.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    # LeetCode problem pages contain one of these words.
    for difficulty in ["Easy", "Medium", "Hard"]:
        if re.search(
            rf"(?<![A-Za-z]){difficulty}(?![A-Za-z])",
            content,
            re.IGNORECASE
        ):
            return difficulty

    return "Unknown"


def get_problems():
    """Find all LeetSync problem folders."""

    problems = []

    for folder in ROOT.iterdir():

        if not folder.is_dir():
            continue

        match = PROBLEM_PATTERN.match(folder.name)

        if not match:
            continue

        number = int(match.group(1))

        title = match.group(2)
        title = title.replace("-", " ")
        title = title.replace("_", " ")
        title = title.title()

        difficulty = get_difficulty(folder)

        problems.append({
            "number": number,
            "title": title,
            "difficulty": difficulty,
            "folder": folder.name
        })

    return sorted(
        problems,
        key=lambda problem: problem["number"]
    )


def difficulty_emoji(difficulty):
    return {
        "Easy": "🟢",
        "Medium": "🟡",
        "Hard": "🔴",
        "Unknown": "⚪"
    }.get(difficulty, "⚪")


def generate_stats(problems):

    counts = Counter(
        problem["difficulty"]
        for problem in problems
    )

    easy = counts["Easy"]
    medium = counts["Medium"]
    hard = counts["Hard"]
    unknown = counts["Unknown"]

    total = len(problems)

    return f"""### 🧩 Problems Solved

| Difficulty | Problems |
|:---:|---:|
| 🟢 Easy | **{easy}** |
| 🟡 Medium | **{medium}** |
| 🔴 Hard | **{hard}** |
| ⚪ Unknown | **{unknown}** |
| **🏆 Total** | **{total}** |

### 📈 Progress

```text
🟢 Easy       {easy}
🟡 Medium     {medium}
🔴 Hard       {hard}
⚪ Unknown    {unknown}

🏆 TOTAL      {total}
"""
