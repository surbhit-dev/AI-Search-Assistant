# 🔥 AI Search Assistant

An AI-powered search engine that searches the web, extracts relevant content, ranks information, and generates concise answers using Google's Gemini model.

## Project Overview

Traditional search engines return links.

AI Search Assistant goes one step further by retrieving web content, processing it, identifying the most relevant information, and generating a direct answer for the user.

The project was built to understand how modern AI search systems and Retrieval-Augmented Generation (RAG) architectures work behind the scenes.

---

## Demo Workflow

```text
User Query
    ↓
DuckDuckGo Search
    ↓
URL Discovery
    ↓
Content Extraction
    ↓
Text Chunking
    ↓
Relevance Ranking
    ↓
Gemini AI
    ↓
Final Answer + Sources
```

---

## System Architecture

```text
┌─────────────────────┐
│ Angular Frontend    │
└──────────┬──────────┘
           │ HTTP Request
           ▼
┌─────────────────────┐
│ FastAPI Backend     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ DuckDuckGo Search   │
└──────────┬──────────┘
           │ URLs
           ▼
┌─────────────────────┐
│ Content Extractor   │
└──────────┬──────────┘
           │ Raw Text
           ▼
┌─────────────────────┐
│ Chunker             │
└──────────┬──────────┘
           │ Chunks
           ▼
┌─────────────────────┐
│ Ranker              │
└──────────┬──────────┘
           │ Best Chunks
           ▼
┌─────────────────────┐
│ Gemini AI           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Final Answer        │
└─────────────────────┘
```

---

## Data Flow

```text
Question:
"What is Retrieval-Augmented Generation?"

↓

Search Engine finds relevant pages

↓

Web pages are downloaded

↓

Content is extracted and cleaned

↓

Text is divided into chunks

↓

Chunks are scored for relevance

↓

Highest scoring chunks are selected

↓

Gemini generates an answer

↓

Answer is displayed in Angular UI
```

---

## Features

* Web search integration
* Content extraction from webpages
* Content chunking
* Relevance-based ranking
* AI answer generation
* Angular frontend
* FastAPI backend
* Source display
* Gemini integration

---

## Tech Stack

### Frontend

* Angular 18
* TypeScript
* HTML
* CSS

### Backend

* Python
* FastAPI
* Requests
* BeautifulSoup
* DuckDuckGo Search

### AI

* Google Gemini

### Utilities

* Python Dotenv

---

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
│   ├── src
│   └── Angular Application
│
├── api.py
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

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

Run backend:

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

---

## Learning Objectives

This project was created to gain hands-on experience with:

* Search engine architecture
* Information retrieval systems
* Content extraction pipelines
* Retrieval-Augmented Generation (RAG)
* LLM integration
* Full-stack AI applications
* Angular and FastAPI integration

---

## Current Pipeline

Implemented:

* Search
* Extraction
* Chunking
* Ranking
* AI Answer Generation
* Source Display

---

## Future Improvements

* Better citation support
* Multi-source answer synthesis
* Streaming responses
* Improved ranking algorithms
* Search history
* Authentication
* Vector database integration
* Advanced UI and animations
* Source credibility scoring

---

## Interview Discussion Topics

This project demonstrates:

### Information Retrieval

How search engines discover and process information.

### Ranking Systems

How relevant content is selected from large amounts of text.

### Retrieval-Augmented Generation (RAG)

Combining external knowledge sources with LLMs.

### Full Stack Development

Building and integrating frontend, backend, and AI services.

### AI Engineering

Prompt design, context selection, and answer generation.

---

## Author

**Surbhit dev**

AI Search Assistant was built as a learning project to understand the architecture behind modern AI-powered search systems.
