import string
from typing import Any
from unittest import result

from .search_utils import load_movies, DEFAULT_SEARCH_LIMIT, Movie

def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[Movie]:
    """
    Search for movies using the BM25 algorithm.

    Args:
        query (str): The search query.
        limit (int): The maximum number of results to return.

    Returns:
        list[dict]: A list of search results, each represented as a dictionary.
    """
    movies = load_movies()
    # Placeholder for actual BM25 search implementation
    # For now, we will return a simple filtered list based on the query
    preprocess_queries = preprocess_text(query)
    results: list[Movie] = []
    for movie in movies:
        query_tokens = tokenize_text(query)
        title_tokens = tokenize_text(movie["title"])
        if has_matching_token(query_tokens, title_tokens):
            results.append(movie)
    return results[:limit]

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    return text

def tokenize_text(text: str) -> list[str]:
    text = preprocess_text(text)
    tokens = text.split()
    valid_tokens = []
    for token in tokens:
        if token:
            valid_tokens.append(token)
    return valid_tokens

def has_matching_token(query_tokens: list[str], title_tokens: list[str]) -> bool:
    for query_token in query_tokens:
        for title_token in title_tokens:
            if query_token in title_token:
                return True
    return False