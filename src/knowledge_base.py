import json
import os
from .extractor import extract_entities, extract_relationships

class KnowledgeBase:
    def __init__(self):
        self.entities = {} # name -> type
        self.relationships = []
        self.mentions = {} # entity_name -> count

    def add_text(self, text):
        ents = extract_entities(text)
        for e in ents:
            name = e["name"]
            self.entities[name] = e["type"]
            self.mentions[name] = self.mentions.get(name, 0) + 1
            
        rels = extract_relationships(text, ents)
        for r in rels:
            if r not in self.relationships:
                self.relationships.append(r)

    def load_raw_data(self, filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
            for thread in data:
                self.add_text(thread['title'])
                self.add_text(thread['body'])
                for comment in thread['comments']:
                    self.add_text(comment)

    def export_state(self, filepath):
        state = {
            "entities": self.entities,
            "relationships": self.relationships,
            "mentions_count": self.mentions
        }
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)

    def load_state(self, filepath):
        with open(filepath, 'r') as f:
            state = json.load(f)
            self.entities = state["entities"]
            self.relationships = state["relationships"]
            self.mentions = state.get("mentions_count", {})

    def reason(self, input_text):
        ents = extract_entities(input_text)
        if not ents:
            return "No known entities found in the input."
            
        response = "Based on the knowledge base:\n"
        for e in ents:
            name = e["name"]
            e_type = e["type"]
            response += f"\n- Input mentions **{name}** (a {e_type}).\n"
            
            related = [r for r in self.relationships if r["source"] == name or r["target"] == name]
            if related:
                response += "  It is related to:\n"
                for r in related:
                    other = r["target"] if r["source"] == name else r["source"]
                    rel = r["relation"]
                    response += f"    - {other} ({rel})\n"
            else:
                response += "  I don't have strong relationships mapped for this yet.\n"
                
        return response
