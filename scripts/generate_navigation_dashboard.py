import os

SECTIONS = {
    "Entries": "entries",
    "Echoes": "echos",
    "Ontology": "ontology",
    "Protocols": "protocols",
    "Tools": "tools",
    "Milestones": "milestones",
    "Core Principles": "core-principles",
    "Meta Docs": "meta/readmes",
}

OUTPUT_FILE = "meta/index/navigation_dashboard.md"

def collect_links():
    dashboard = ["# 🧭 Codex Navigation Dashboard\n"]
    for label, folder in SECTIONS.items():
        if not os.path.exists(folder):
            continue
        files = sorted([f for f in os.listdir(folder) if f.endswith(".md")])
        if not files:
            continue
        das

cat << 'EOF' > scripts/generate_navigation_dashboard.py
import os

SECTIONS = {
    "Entries": "entries",
    "Echoes": "echos",
    "Ontology": "ontology",
    "Protocols": "protocols",
    "Tools": "tools",
    "Milestones": "milestones",
    "Core Principles": "core-principles",
    "Meta Docs": "meta/readmes",
}

OUTPUT_FILE = "meta/index/navigation_dashboard.md"

def collect_links():
    dashboard = ["# 🧭 Codex Navigation Dashboard\n"]
    for label, folder in SECTIONS.items():
        if not os.path.exists(folder):
            continue
        files = sorted([f for f in os.listdir(folder) if f.endswith(".md")])
        if not files:
            continue
        dashboard.append(f"\n## {label}\n")
        for f in files:
            name = f.replace("_", " ").replace(".md", "")
            path = os.path.join(folder, f).replace("\\", "/")
            dashboard.append(f"- [{name}]({path})")
    return "\n".join(dashboard)

def build_dashboard():
    content = collect_links()
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Navigation dashboard generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    build_dashboard()
