from .search_utils import load_movies, DEFAULT_SEARCH_LIMIT, Movie, tokenize_text


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


def has_matching_token(query_tokens: list[str], title_tokens: list[str]) -> bool:
    for query_token in query_tokens:
        for title_token in title_tokens:
            if query_token in title_token:
                return True
    return False
