import json
import yaml
import os
from collections import defaultdict

def build_semantic_index(ontology_path="build/ontology.json", output_file="build/tag_index.yaml"):
    # Create directory if not exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        with open(ontology_path, 'r') as f:
            nodes = json.load(f)
    except FileNotFoundError:
        print("❌ Ontology file not found. Run parse_ontology.py first.")
        return
    
    tag_index = defaultdict(list)
    
    for node in nodes:
        if 'tags' in node:
            for tag in node['tags']:
                tag_index[tag].append({
                    "id": node["id"],
                    "title": node["title"]
                })
    
    index = {
        "tags": dict(tag_index),
        "metadata": {
            "total_tags": len(tag_index),
            "total_nodes": len(nodes)
        }
    }
    
    with open(output_file, 'w') as f:
        yaml.dump(index, f, sort_keys=False)
    
    print(f"✅ Built semantic index with {len(nodes)} nodes at {output_file}")

if __name__ == "__main__":
    build_semantic_index()
