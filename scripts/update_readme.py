from pathlib import Path
from collections import Counter
from datetime import datetime
import re

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

PROBLEM_PATTERN = re.compile(r"^(\d+)-(.+)$")

LANG_MAPPING = {
    ".py": "Python",
    ".java": "Java",
    ".cpp": "C++",
    ".cc": "C++",
    ".c": "C",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".go": "Go",
    ".rs": "Rust",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".cs": "C#",
    ".rb": "Ruby",
    ".php": "PHP",
    ".sql": "SQL",
    ".scala": "Scala"
}


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
```"""


def generate_problems_table(problems):
    """Generate markdown table for all solved problems."""
    
    table = [
        "| # | Title | Solution | Difficulty |",
        "| :---: | :--- | :--- | :--- |"
    ]
    
    for problem in problems:
        # Title link pointing to the folder
        title_link = f"[{problem['title']}](./{problem['folder']})"
        
        # Difficulty with emoji
        diff_emoji = difficulty_emoji(problem['difficulty'])
        diff_str = f"{diff_emoji} {problem['difficulty']}"
        
        # Solutions files within folder
        solution_links = []
        folder_path = ROOT / problem['folder']
        for file in folder_path.iterdir():
            if file.is_file() and file.name.lower() != "readme.md":
                ext = file.suffix.lower()
                lang_name = LANG_MAPPING.get(ext, file.name)
                # Markdown link to file
                solution_links.append(f"[{lang_name}](./{problem['folder']}/{file.name})")
        
        if not solution_links:
            solution_str = f"[Folder](./{problem['folder']})"
        else:
            # Join solutions if there are multiple
            solution_str = ", ".join(solution_links)
            
        table.append(f"| {problem['number']} | {title_link} | {solution_str} | {diff_str} |")
        
    return "\n".join(table)


def main():
    if not README.exists():
        print(f"Error: {README} does not exist.")
        return

    content = README.read_text(encoding="utf-8")
    problems = get_problems()

    # Generate stats and problems table
    stats_content = generate_stats(problems)
    problems_table = generate_problems_table(problems)

    # Regex search/replace with boundary markers
    stats_pattern = re.compile(
        r"(<!--\s*STATS_START\s*-->).*?(<!--\s*STATS_END\s*-->)",
        re.DOTALL
    )
    new_content = stats_pattern.sub(
        f"\\1\n\n{stats_content}\n\n\\2",
        content
    )

    problems_pattern = re.compile(
        r"(<!--\s*PROBLEMS_START\s*-->).*?(<!--\s*PROBLEMS_END\s*-->)",
        re.DOTALL
    )
    new_content = problems_pattern.sub(
        f"\\1\n\n{problems_table}\n\n\\2",
        new_content
    )

    README.write_text(new_content, encoding="utf-8")
    print(f"Successfully updated README.md with stats and {len(problems)} problems.")


if __name__ == "__main__":
    main()
