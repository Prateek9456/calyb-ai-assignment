# Reddit Knowledge Base: LLM Deployment

This project transforms unstructured Reddit discussions about LLM deployment into a structured knowledge graph that can be reasoned over.

## Structure
- `src/extractor.py`: Custom rule-based entity and relationship extractor.
- `src/knowledge_base.py`: The core class that builds the graph and persists it.
- `src/cli.py`: Testable interface to query the knowledge state.
- `data/raw_data.json`: A static, focused subset of Reddit threads around LLM deployment.
- `data/knowledge_state.json`: The serialized knowledge graph.

## Setup
No external dependencies are required. This project uses pure Python standard libraries to adhere to the constraint of not using auto-extraction tools.

## Running the Project

**1. Regenerate the knowledge state:**
```bash
python -m src.cli --build
```

**2. Query the system with a new input:**
```bash
python -m src.cli --query "I am looking for high throughput and continuous batching, but I'm worried about OOM"
```
