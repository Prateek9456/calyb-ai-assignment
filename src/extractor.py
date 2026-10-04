import re

ENTITIES = {
    "Tool": ["vLLM", "TensorRT-LLM", "TGI", "HuggingFace TGI", "Triton"],
    "Concept": ["throughput", "latency", "PagedAttention", "quantization", "AWQ", "GPTQ", "KV cache", "continuous batching", "concurrent requests", "batch size"],
    "Problem": ["OOM", "Out Of Memory", "crashing"],
    "Model": ["Llama-3 70B", "Llama 3"]
}

def extract_entities(text):
    found = []
    text_lower = text.lower()
    for ent_type, words in ENTITIES.items():
        for word in words:
            if re.search(r'\b' + re.escape(word.lower()) + r'\b', text_lower):
                found.append({"type": ent_type, "name": word})
    return found

def extract_relationships(text, entities):
    relationships = []
    text_lower = text.lower()
    
    tools = [e["name"] for e in entities if e["type"] == "Tool"]
    concepts = [e["name"] for e in entities if e["type"] == "Concept"]
    problems = [e["name"] for e in entities if e["type"] == "Problem"]
    
    if "handled" in text_lower or "solves" in text_lower or "better" in text_lower or "without" in text_lower:
        for t in tools:
            for p in problems:
                relationships.append({"source": t, "target": p, "relation": "MIGHT_SOLVE"})
    
    for t in tools:
        for c in concepts:
            if c.lower() in text_lower and t.lower() in text_lower:
                relationships.append({"source": t, "target": c, "relation": "ASSOCIATED_WITH"})
                
    for p in problems:
        for c in concepts:
            if c.lower() in text_lower and p.lower() in text_lower:
                relationships.append({"source": p, "target": c, "relation": "RELATED_TO_CONCEPT"})

    return relationships
