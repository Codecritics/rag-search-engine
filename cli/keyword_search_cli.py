import argparse

from lib.keyword_search import search_command
from lib.keyword_build import build_command
from lib.keyword_tf import tf_command

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    build_parser = subparsers.add_parser("build", help="Build the inverted index")
    tf_parser = subparsers.add_parser("tf", help="Get the term frequency of a term")
    tf_parser.add_argument("doc_id", type=int, help="Document ID")
    tf_parser.add_argument("term", type=str, help="Term")
    args = parser.parse_args()

    match args.command:
        case "search":
            print("Searching for:", args.query)
            results = search_command(args.query)
            for i, res in enumerate(results, 1):
                print(f"- '{res['title']}'")
        case "build":
            print("Building inverted index")
            index = build_command()
            print("Inverted index built successfully.")
        case "tf":
            print(f"Getting term frequency for term '{args.term}' in document ID {args.doc_id}")
            tf = tf_command(args.doc_id, args.term)
            print(f"Term frequency: {tf}")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
