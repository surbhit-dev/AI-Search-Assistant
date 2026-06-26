# AI Search Assistant

An AI-powered search engine that searches the web, extracts relevant content, ranks information, and generates concise answers using Google's Gemini model.

## Overview

AI Search Assistant combines web search, content extraction, intelligent ranking, and Large Language Models (LLMs) to provide direct answers from web content instead of simply returning links.

The project was built to explore the architecture behind modern AI search systems and retrieval-augmented generation (RAG) workflows.

## Features

* Web search using DuckDuckGo
* Automatic webpage content extraction
* Content chunking for efficient processing
* Relevance-based chunk ranking
* AI-generated answers using Gemini
* Angular frontend interface
* Source tracking and display
* FastAPI backend

## Architecture

User Query
↓
DuckDuckGo Search
↓
Content Extraction
↓
Content Chunking
↓
Chunk Ranking
↓
Gemini AI
↓
Answer + Sources

## Tech Stack

### Backend

* Python
* FastAPI
* DuckDuckGo Search (DDGS)
* BeautifulSoup
* Requests
* Google Gemini API

### Frontend

* Angular 18
* TypeScript
* HTML
* CSS

## Project Structure

```text
AI-Search-Assistant
│
├── core
│   ├── url_discovery.py
│   ├── content_extractor.py
│   ├── chunker.py
│   ├── ranker.py
│   ├── response_generator.py
│   └── search_pipeline.py
│
├── frontend
│   └── Angular Application
│
├── api.py
├── app.py
├── config.py
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/surbhit-dev/AI-Search-Assistant.git
cd AI-Search-Assistant
```

### Backend Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the backend:

```bash
python api.py
```

### Frontend Setup

```bash
cd frontend
npm install
ng serve
```

Open:

```text
http://localhost:4200
```

## Learning Goals

This project was created to understand:

* Search engine pipelines
* Information retrieval
* Content extraction
* Retrieval-Augmented Generation (RAG)
* LLM integration
* Full-stack AI application development

## Current Status

Current pipeline:

* Search
* Extract
* Chunk
* Rank
* Generate Answer

The project is actively being improved with UI enhancements, source attribution improvements, and additional search capabilities.

## Future Improvements

* Better source citations
* Improved ranking algorithms
* Multi-source answer synthesis
* Advanced UI design
* Streaming responses
* Search history
* User authentication
* Vector database integration

## Author

Surbhit Srivas

Built as a learning project exploring modern AI search architectures.
