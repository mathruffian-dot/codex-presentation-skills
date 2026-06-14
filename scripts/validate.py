from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ("pptx-teaching-deck", "html-slide-deck")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


for path in ROOT.rglob("*"):
    if path.is_file() and ".git" not in path.parts:
        try:
            path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            fail(f"{path} is not UTF-8: {exc}")

for name in SKILLS:
    skill_file = ROOT / "skills" / name / "SKILL.md"
    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{skill_file} has invalid frontmatter")
    frontmatter = match.group(1)
    if f"name: {name}" not in frontmatter:
        fail(f"{skill_file} name does not match folder")
    if "description:" not in frontmatter:
        fail(f"{skill_file} is missing description")

html = (ROOT / "skills" / "html-slide-deck" / "assets" / "starter" / "index.html").read_text(
    encoding="utf-8"
)
checks = {
    "balanced section tags": html.count("<section") == html.count("</section>"),
    "keyboard navigation": "ArrowRight" in html and "Home" in html and "End" in html,
    "print mode": "@media print" in html,
    "hash navigation": "history.replaceState" in html,
    "speaker notes": 'class="notes"' in html,
}
for label, passed in checks.items():
    if not passed:
        fail(f"HTML starter failed: {label}")

print("Validation passed.")
