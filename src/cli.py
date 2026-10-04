import argparse
from src.knowledge_base import KnowledgeBase

def main():
    parser = argparse.ArgumentParser(description="Query the Reddit Knowledge Base")
    parser.add_argument("--query", type=str, help="Question or situation to reason over")
    parser.add_argument("--build", action="store_true", help="Rebuild the knowledge base from raw data")
    args = parser.parse_args()

    kb = KnowledgeBase()
    
    if args.build:
        print("Building knowledge base...")
        kb.load_raw_data("data/raw_data.json")
        kb.export_state("data/knowledge_state.json")
        print("Done. Saved to data/knowledge_state.json")
    else:
        try:
            kb.load_state("data/knowledge_state.json")
        except FileNotFoundError:
            print("Knowledge state not found. Please run with --build first.")
            return

        if args.query:
            print(f"Input: {args.query}\n")
            output = kb.reason(args.query)
            print(output)
        else:
            print("Please provide a --query to reason over.")

if __name__ == "__main__":
    main()
