from .build_utils import InvertedIndex
from .search_utils import tokenize_text


def tf_command(doc_id: int, term: str) -> int:
    """
    Retrieves the term frequency of a given term in a specific document.
    """
    token = tokenize_single_term(term)
    index = InvertedIndex()
    index.load()
    return index.get_tf(doc_id, token)


def tokenize_single_term(term: str) -> str:
    """
    Tokenize a term and require it to produce exactly one token.

    Args:
        term (str): The term to be tokenized.

    Returns:
        str: The tokenized term.
    """
    tokens = tokenize_text(term)
    if len(tokens) != 1:
        raise ValueError(
            f"Expected a single token, but got {len(tokens)} tokens: {tokens}"
        )
    return tokens[0]
