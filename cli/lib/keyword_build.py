from .build_utils import InvertedIndex

def build_command() -> InvertedIndex:
    """
    Build the inverted index for the movie dataset.

    Returns:
        InvertedIndex: The constructed inverted index.
    """
    index = InvertedIndex()
    index.build()
    index.save()
    docs = index.get_documents("merida")
    if docs:
        print(f"First document ID for token 'merida' = {docs[0]}")

    return index