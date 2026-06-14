from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILLS = (
    "pptx-teaching-deck",
    "html-slide-deck",
    "image-poster-deck",
    "image-editable-deck",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".html", ".py", ".ps1", ".txt", ""}

for path in ROOT.rglob("*"):
    if (
        path.is_file()
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and path.suffix.lower() in TEXT_SUFFIXES
    ):
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
    agent_file = ROOT / "skills" / name / "agents" / "openai.yaml"
    if not agent_file.exists():
        fail(f"{name} is missing agents/openai.yaml")

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

for name in ("image-poster-deck", "image-editable-deck"):
    script = ROOT / "skills" / name / "scripts" / "pack_pptx.py"
    if not script.exists():
        fail(f"{name} is missing pack_pptx.py")

print("Validation passed.")
