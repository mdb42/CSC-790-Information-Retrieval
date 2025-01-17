# InfoQuest

A desktop application that demonstrates core Information Retrieval (IR) concepts through an interactive interface.

## Overview

InfoQuest illustrates how search engines work, from document collection to query processing. Built with PyQt6, it implements the classic IR pipeline:

1. Document Collection (web crawling and local imports)
2. Document Processing & Indexing
3. Query Processing & Retrieval

## Features

### Document Collection
- Web crawler with configurable search depth and breadth
- Customizable crawl speeds and domain restrictions
- Local file importing and management

### Document Processing & Indexing
- Text processing options:
  - Case sensitivity
  - Stop word filtering
  - Multiple stemming algorithms
- Ranking schemes:
  - TF-IDF (term frequency-inverse document frequency)
  - BM25 (Okapi BM25 ranking)
  - PageRank (for web document collections)

### Search & Retrieval
- Interactive search interface
- Query process visualization (verbose mode)
- Content-aware ranking (weights for titles, headings, body text)

## Interface

The application uses a dockable widget design:
- Left dock: Web crawler controls
- Center: Search interface and results
- Right dock: Document indexing tools

## Installation

### Prerequisites
- Python 3.8+
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/yourusername/infoquest.git
cd infoquest

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

For troubleshooting, see our [Issues](https://github.com/yourusername/infoquest/issues) page.

## Quick Start

1. Launch InfoQuest
2. Create or open a project
3. Configure indexing settings
4. Import documents (local) or start web crawler
5. Build the index
6. Search and explore results

## About

InfoQuest was developed as part of graduate studies in Information Retrieval, implementing concepts from Manning, Raghavan, and Schütze's "Introduction to Information Retrieval." The project is in active development, focusing on educational value and practical demonstration of IR concepts.

## License

Released under GPL v3. See [LICENSE.md](LICENSE.md) for details.

## Acknowledgments

- Built with PyQt6
- Developed for CSC790 Information Retrieval
- Based on "Introduction to Information Retrieval" concepts