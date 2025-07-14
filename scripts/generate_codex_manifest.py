import os
import yaml

ENTRIES_DIR = "entries"
MANIFEST_PATH = "meta/index/codex_manifest.yaml"

def extract_title(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                return line.strip().lstrip("#").strip()
    return "Untitled"

def build_manifest():
    manifest = []

    for filename in sorted(os.listdir(ENTRIES_DIR)):
        if filename.startswith("entry_") and filename.endswith(".md"):
            entry_id = filename.replace("entry_", "").replace(".md", "")
            title = extract_title(os.path.join(ENTRIES_DIR, filename))
            entry = {
                "id": entry_id,
                "title": title,
                "tags": [],
                "linked_entries": []
            }
            manifest.append(entry)

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False)

    print(f"✅ Codex manifest generated at {MANIFEST_PATH}")

if __name__ == "__main__":
    build_manifest()
