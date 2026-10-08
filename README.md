# Document Summarizer

## Project Overview

This project is a document summarization application that processes PDF documents, extracts their content, divides the content into manageable chunks, and generates concise summaries using an LLM-based workflow.

The project follows a modular architecture with separate components for document ingestion, processing, summarization, and workflow orchestration.

## Key Features

- PDF document ingestion
- Text extraction from PDF documents
- Document chunking for efficient processing
- LLM-based document summarization
- Modular processing pipeline
- Graph-based workflow orchestration
- Configurable application settings
- Python-based implementation

## Project Workflow

```text
PDF Document
     ↓
PDF Reader
     ↓
Text Extraction
     ↓
Document Chunking
     ↓
Summarization
     ↓
Workflow / Graph Orchestration
     ↓
Final Summary
```

## Technologies Used

- Python
- PDF Processing
- LangGraph
- LLM-based Summarization
- Document Chunking
- Graph-based Workflow
- Modular Python Architecture

## Project Structure

```text
Doc_summarizer/
│
├── Summarizer/
│   └── summarize.py
│
├── graph/
│   ├── graph_builder.py
│   ├── nodes.py
│   └── state.py
│
├── ingestion/
│   └── pdf_reader.py
│
├── processing/
│   └── chunking.py
│
├── config.py
├── main.py
├── test.py
├── README.md
└── .gitignore
```

## Setup

Clone the repository:

```bash
git clone https://github.com/art-5688/document_summarizer.git
```

Navigate to the project:

```bash
cd document_summarizer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies according to the project's configuration.

## Environment Variables

Create a `.env` file locally for required API keys or configuration values.

**Do not commit `.env` to GitHub.**

The `.gitignore` file is configured to exclude it from version control.

## ▶️ Running the Project

Run the application using:

```bash
python main.py
```

## Key Learning Outcomes

This project demonstrates practical experience with:

- Document ingestion pipelines
- PDF text extraction
- Text chunking
- LLM-powered summarization
- LangGraph workflow orchestration
- Modular application design
- Configuration management
- Building a reusable document-processing pipeline

## Future Improvements

- Support multiple document formats
- Add a Streamlit-based user interface
- Add document-level and section-level summaries
- Add summarization quality evaluation
- Add asynchronous document processing
- Add Docker support
- Add API-based access using FastAPI

## Author

**Aishwarya Teke**

GitHub: https://github.com/art-5688