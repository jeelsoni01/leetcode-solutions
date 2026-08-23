from pathlib import Path
from collections import Counter
from datetime import datetime
import re


ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"


DIFFICULTIES = ["Easy", "Medium", "Hard"]


def get_problems():
    problems = []

    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue

        if ".git" in path.parts:
            continue

        if path.suffix not in {".py", ".cpp", ".java", ".js", ".ts"}:
            continue

        parts = path.relative_to(ROOT).parts

        difficulty = next(
            (x for x in parts if x in DIFFICULTIES),
            None
        )

        if difficulty is None:
            continue

        match = re.match(r"(\d+)[-_](.+)", path.stem)

        if not match:
            continue

        number = int(match.group(1))
        title = match.group(2)

        title = title.replace("-", " ")
        title = title.replace("_", " ")
        title = title.title()

        problems.append({
            "number": number,
            "title": title,
            "difficulty": difficulty,
            "path": path.relative_to(ROOT).as_posix()
        })

    return sorted(problems, key=lambda x: x["number"])


def generate_stats(problems):
    counts = Counter(p["difficulty"] for p in problems)

    total = len(problems)

    easy = counts["Easy"]
    medium = counts["Medium"]
    hard = counts["Hard"]

    return f"""
## 📊 LeetCode Progress

| Metric | Count |
|---|---:|
| 🧩 **Total Solved** | **{total}** |
| 🟢 Easy | **{easy}** |
| 🟡 Medium | **{medium}** |
| 🔴 Hard | **{hard}** |

### 📈 Difficulty Distribution

```text
🟢 Easy    {easy}
🟡 Medium  {medium}
🔴 Hard    {hard}
