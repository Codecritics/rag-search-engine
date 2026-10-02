from .search_utils import load_movies, DEFAULT_SEARCH_LIMIT

def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
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
    results = [movie for movie in movies if query.lower() in movie["title"].lower()]
    return results[:limit]