import json
import os
import string
from typing import Any, TypedDict

from nltk.stem import PorterStemmer

PROJECT_ROOT: Any = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")
STOPWORD_PATH = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")
DEFAULT_SEARCH_LIMIT = 10


def preprocess_text(text: str) -> str:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


def load_stopwords() -> list[str]:
    with open(STOPWORD_PATH, "r", encoding="utf-8") as f:
        return [preprocess_text(word) for word in f.read().splitlines()]


STOPWORDS = load_stopwords()


def tokenize_text(text: str) -> list[str]:
    text = preprocess_text(text)
    tokens = [t for t in text.split() if t]
    filtered = [w for w in tokens if w not in STOPWORDS]
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in filtered]


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