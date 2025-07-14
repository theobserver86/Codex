import json
import re
import random

class RecursiveQueryEngine:
    def __init__(self, ontology_path="build/ontology.json"):
        try:
            with open(ontology_path, 'r') as f:
                self.ontology = json.load(f)
            print(f"✅ Loaded {len(self.ontology)} ontology nodes")
        except FileNotFoundError:
            print("⚠️ Ontology file not found. Using sample data.")
            self.ontology = [{
                "id": "sample_001",
                "title": "Sample Node",
                "tags": ["test"],
                "summary": "Sample summary",
                "content": "Sample content"
            }]
    
    def find_ontology_matches(self, query):
        tokens = re.findall(r'\w+', query.lower())
        matches = []
        
        for node in self.ontology:
            content = (node.get('title', '') + " " + node.get('summary', '')).lower()
            if any(token in content for token in tokens):
                matches.append(node)
        
        return matches[:3]
    
    def find_related_patterns(self, matches):
        related = []
        for node in matches:
            related.append({
                "pattern": f"Δ-{node.get('id', 'id_missing').upper()}",
                "description": f"Recursive pattern based on {node.get('title', 'Untitled')}",
                "strength": random.uniform(0.5, 1.0)
            })
        return related
    
    def generate_reflection(self, matches):
        if not matches:
            return "🌀 The signal remains uncaught. Refine your query."
        
        base = matches[0]
        title = base.get('title', 'Untitled Node')
        symbol = base.get('symbol', '🌀')  # Default symbol if missing
        
        reflection = f"**{title}** ({symbol})\n\n"
        reflection += f"{base.get('summary', 'No summary available')}\n\n"
        reflection += "*Recursive insights:*\n"
        
        insights = [
            f"- This concept mirrors {random.choice(['knowledge decomposition', 'semantic recursion'])}",
            f"- Consider the {random.choice(['inverse', 'complementary'])} pattern: ◊{random.randint(1,9)}"
        ]
        
        return reflection + "\n".join(insights[:random.randint(2,3)])
    
    def query(self, question):
        print(f"🔍 Query: '{question}'")
        
        matches = self.find_ontology_matches(question)
        print(f"📚 Matched {len(matches)} ontology nodes")
        
        patterns = self.find_related_patterns(matches)
        print(f"🌀 Found {len(patterns)} related patterns")
        
        reflection = self.generate_reflection(matches)
        
        return {
            "query": question,
            "matches": [{"id": m.get("id", "N/A"), "title": m.get("title", "Untitled")} for m in matches],
            "patterns": patterns,
            "reflection": reflection
        }

if __name__ == "__main__":
    engine = RecursiveQueryEngine()
    test_question = "How does recursive reflection work in knowledge systems?"
    result = engine.query(test_question)
    
    print("\n=== RESULT ===")
    print(f"Reflection:\n{result['reflection']}")
