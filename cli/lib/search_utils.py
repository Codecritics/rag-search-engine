import json
import os
from typing import Any, TypedDict

class Movie(TypedDict):
    id: int
    title: str
    description: str

class SearchResult(TypedDict):
    id: int
    title: str
    score: float
    metadata: dict[str, Any]

def load_movies() -> list[Movie]:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["movies"]


PROJECT_ROOT: Any = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")
STOPWORD_PATH = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")
DEFAULT_SEARCH_LIMIT = 10