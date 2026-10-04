import string
from typing import Any
from unittest import result
from nltk.stem import PorterStemmer

from .search_utils import load_movies, STOPWORD_PATH, DEFAULT_SEARCH_LIMIT, Movie


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
    results: list[Movie] = []
    query_tokens = tokenize_text(query)
    print(query_tokens)
    for movie in movies:
        title_tokens = tokenize_text(movie["title"])
        if has_matching_token(query_tokens, title_tokens):
            results.append(movie)
    return results[:limit]

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def load_stopwords() -> list[str]:
    with open(STOPWORD_PATH, "r", encoding="utf-8") as f:
        stopwords = [preprocess_text(word) for word in f.read().splitlines()]
    return stopwords


STOPWORDS = load_stopwords()
def tokenize_text(text: str) -> list[str]:
    text = preprocess_text(text)
    tokens = text.split()
    valid_tokens = []
    for token in tokens:
        if token:
            valid_tokens.append(token)
    filtered_words = []

    for word in valid_tokens:
        if word not in STOPWORDS:

            filtered_words.append(word)
    stemmer = PorterStemmer()
    stemmed_words = []
    for word in filtered_words:
        stemmed_words.append(stemmer.stem(word))
    return stemmed_words

def has_matching_token(query_tokens: list[str], title_tokens: list[str]) -> bool:
    for query_token in query_tokens:
        for title_token in title_tokens:
            if query_token in title_token:
                return True
    return False
