import glob
import frontmatter
import json
import os
import yaml
from pathlib import Path

def parse_ontology_files(input_path="ontology/*.md", output_format="json"):
    # Create build directory if not exists
    os.makedirs("build", exist_ok=True)
    
    ontology_nodes = []
    processed_count = 0
    error_count = 0
    
    for file_path in glob.glob(input_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                
                node = {
                    "id": Path(file_path).stem,
                    "title": post.metadata.get('title', ''),
                    "tags": post.metadata.get('tags', []),
                    "summary": post.metadata.get('summary', ''),
                    "content": post.content,
                    "file_path": file_path
                }
                
                # Optional fields
                for field in ['symbol', 'relations']:
                    if field in post.metadata:
                        node[field] = post.metadata[field]
                
                ontology_nodes.append(node)
                processed_count += 1
        except Exception as e:
            print(f"⚠️ Error processing {file_path}: {str(e)}")
            error_count += 1
    
    if output_format == "json":
        with open('build/ontology.json', 'w') as f:
            json.dump(ontology_nodes, f, indent=2)
    else:
        with open('build/ontology.yaml', 'w') as f:
            yaml.dump(ontology_nodes, f, sort_keys=False)
    
    print(f"✅ Successfully processed {processed_count} files, {error_count} errors")
    return ontology_nodes

if __name__ == "__main__":
    nodes = parse_ontology_files(output_format="json")
