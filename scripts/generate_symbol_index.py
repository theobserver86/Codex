import os

ENTRIES_DIR = "entries"
OUTPUT_FILE = "symbol_index.md"

def extract_title(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().lower().startswith("#"):
                return line.strip("# \n")
    return "Untitled"

def build_index():
    entries = []
    for filename in sorted(os.listdir(ENTRIES_DIR)):
        if filename.endswith(".md") and filename.startswith("entry_"):
            path = os.path.join(ENTRIES_DIR, filename)
            title = extract_title(path)
            entries.append(f"- [{filename}](entries/{filename}) — **{title}**")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# 🧿 Codex Symbol Index\n\n")
        f.write("\n".join(entries))

    print(f"✅ Symbol index generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    build_index()
