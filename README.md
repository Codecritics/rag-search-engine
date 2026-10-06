# Movie Keyword Search

A command-line movie search tool backed by a local inverted index. It preprocesses movie titles and descriptions, then lets you search the collection or inspect how often a term appears in a particular movie.

> The repository currently implements lexical keyword search, not a complete retrieval-augmented generation (RAG) pipeline. Search uses token matches; it does not generate answers or calculate BM25 relevance scores.

## Features

- Builds an inverted index from movie titles and descriptions.
- Normalizes text to lowercase, removes punctuation and stopwords, and applies Porter stemming.
- Searches for movies containing any of the query's remaining stemmed tokens.
- Reports the frequency of a token in a movie document.
- Saves the index and document data locally under `cache/`.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

Install the project dependencies with:

```sh
uv sync
```

## Movie data

The indexer expects `data/movies.json` with a top-level `movies` array. Each movie must have an integer `id`, a `title`, and a `description`:

```json
{
  "movies": [
    {
      "id": 1,
      "title": "Example Movie",
      "description": "A short plot description."
    }
  ]
}
```

Stopwords are read from `data/stopwords.txt`, with one word per line. The `data/` directory is ignored by Git, so provide these files locally if they are not already present.

## Usage

Run commands from the project root.

### Build or rebuild the index

Build the local index after adding or changing movie data:

```sh
uv run python cli/keyword_search_cli.py build
```

The command writes `index.pkl`, `docmap.pkl`, and `term_frequencies.pkl` to `cache/`.

### Search movies

Build the index first, then search with a quoted query:

```sh
uv run python cli/keyword_search_cli.py search "space adventure"
```

The search returns up to 10 matching movies, displaying their titles. Query terms are stemmed and stopwords are removed just as they are during indexing. A movie is included if it matches any remaining query term; results are not scored or ranked by relevance.

### Get a term frequency

```sh
uv run python cli/keyword_search_cli.py tf 1 adventure
```

This prints the number of times the normalized term occurs in the movie with ID `1`. The term argument must normalize to exactly one token; punctuation and stopword removal can affect that.

For command help:

```sh
uv run python cli/keyword_search_cli.py --help
```

## Project layout

```text
cli/
  keyword_search_cli.py  Command-line entry point
  lib/
    build_utils.py       Inverted-index storage and lookup
    keyword_build.py     Index-building command
    keyword_search.py    Movie search
    keyword_tf.py        Term-frequency lookup
    search_utils.py      Data loading and text preprocessing
data/                    Local movie data and stopwords (Git-ignored)
cache/                   Generated index files (Git-ignored)

```