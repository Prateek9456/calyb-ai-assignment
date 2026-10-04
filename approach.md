# Approach

## Domain & Data
**Domain:** C. Community Knowledge on Reddit.
**Data Subset:** Discussions around "LLM Deployment in Production" (tools like vLLM, TensorRT-LLM, TGI, and concepts like latency, throughput, OOM).
**Reasoning:** LLM deployment is a rapidly evolving field where best practices are scattered across Reddit comments rather than formal documentation. Practitioners frequently ask similar questions about balancing latency vs throughput and avoiding OOM errors.

## Entities and Relationships
**Entities Modeled:**
- `Tool`: Software libraries used for deployment (e.g., vLLM, TensorRT-LLM, TGI).
- `Concept`: Technical terms related to the domain (e.g., latency, throughput, quantization, AWQ).
- `Problem`: Common issues encountered (e.g., OOM, crashing).
- `Model`: Specific foundation models mentioned.

**Relationships Modeled:**
- `ASSOCIATED_WITH`: A Tool supports or is frequently discussed in the context of a Concept (e.g., vLLM is associated with PagedAttention).
- `MIGHT_SOLVE`: A Tool is mentioned in a context suggesting it handles or resolves a Problem.
- `RELATED_TO_CONCEPT`: A Problem is associated with a Concept (e.g., OOM is related to batch size).

**Tradeoffs:**
- Extracted entities are dictionary-based rather than LLM-based to strictly adhere to the constraint of not using automated tools. This means the system won't generalize to new tools without updating the dictionary.
- Co-occurrence based relationship extraction is simple but might produce false positives compared to a deep syntactic dependency tree analysis.

## Operating on New Inputs
When a user provides a new situation (e.g., "I keep getting OOM when I increase the batch size on vLLM"), the system:
1. Parses the input to extract known entities (`OOM`, `batch size`, `vLLM`).
2. Consults the knowledge graph for stored relationships surrounding these entities.
3. Produces a structured breakdown showing how these entities relate to each other based on historical Reddit discussions, helping the user see that "OOM is related to batch size" and "vLLM might solve OOM/crashing issues".

## Next Steps
- Implement dependency parsing to make relationship extraction more robust (e.g., Subject-Verb-Object triples).
- Add support for entity aliasing (e.g., `Out of Memory` = `OOM`).
- Expand the dictionary or introduce a hybrid model where an LLM expands the dictionary offline.
