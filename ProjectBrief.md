# Project Brief: MindAether

## Project Description

Design and develop an AI-powered local system that ingests your unstructured personal data (PDFs, notes, images, audio, browsing data) and builds a personalized knowledge graph. Users can query this graph in natural language to surface insights, relationships, and references across data types.

The system acts as an AI curator, handling extraction, linking, and semantic understanding — all offline and privacy-first, with support for Mac, Windows, and Linux systems.

## Target User Base

- University Students & Researchers
- Self-Learners & Knowledge Builders
- Startup Founders, Engineers, and Product Managers
- Privacy-Conscious Professionals

## The Problem

- Unstructured digital clutter (notes, documents, screenshots, bookmarks) becomes unsearchable over time.
- Keyword search is weak across formats like scanned PDFs, images, audio notes.
- Users want insight, not just storage — this tool surfaces relationships and context.

## Product Type

CLI Tool + Local Web UI (Streamlit/Gradio)
- CLI for automation / power use; web UI for querying, visualizing the graph

# Tech Stack — Cross-Platform (Mac M1 + Windows)

This project is designed to work seamlessly on both **Mac M1/M2 devices** and **Windows machines** without compatibility issues. All tools and libraries listed below are selected for their cross-platform support and ease of use in local development environments.

---

## Core Tech Stack

| Layer | Tool / Library | Purpose | Compatibility |
|-------|----------------|---------|----------------|
| 🧾 **Document Parsing** | `PyPDF2`, `python-docx`, `pytesseract` | Parse PDFs, DOCX, TXT, and OCR images | ✅ Mac (M1), ✅ Windows |
| 🖼️ **Image Understanding** | `CLIP` via `openCLIP` or `transformers` | Extract embeddings from images for semantic search | ✅ PyTorch on MPS (Mac), ✅ CUDA (Windows) |
| 🔊 **Audio Transcription** | [`whisper`](https://github.com/openai/whisper) | Convert audio files into transcribed text | ✅ CPU/GPU (MPS & CUDA) |
| 🧠 **LLMs / Embeddings** | `sentence-transformers` (`all-MiniLM`, etc.) | Generate vector embeddings for documents & questions | ✅ Platform-agnostic |
| 🧠 **Local LLMs** | `llama-cpp-python` (GGUF models) | Run fast, local LLMs like Phi or Mistral | ✅ Mac (`metal`), ✅ Windows (`cpu`/`cuda`) |
| 🧠 **NER / Extraction** | `spaCy`, optionally OpenAI API | Named Entity Recognition and text-based relationships | ✅ Everywhere |
| 🔗 **Graph Engine** | `networkx`, `pyvis` | Construct and visualize knowledge graphs | ✅ Everywhere |
| 🧭 **Query Layer** | Custom RAG / `langchain` | Ask NL questions over personal data | ✅ Everywhere |
| 🖥️ **CLI** | `typer` | Command-line interface for running modules | ✅ Everywhere |
| 🌐 **Web UI** | `streamlit` or `gradio` | Local web app for UI-based interaction | ✅ Browser-based, platform-independent |
| 🧪 **Testing & Packaging** | `pytest`, `pyinstaller` (optional) | Run tests and optionally create binaries | ✅ Mac & Windows supported |

---

## MVP Features

| Feature                           | Description                                                               |
| --------------------------------- | ------------------------------------------------------------------------- |
| **📄 Document Ingestion**         | Parse `.pdf`, `.docx`, `.txt` files into plain text                       |
| **🧠 Entity Extraction**          | Use `spaCy` (or optionally LLMs) to extract people, orgs, topics          |
| **🖼️ Image Ingestion + Tagging** | Use CLIP to generate semantic embeddings from images                      |
| **🕸️ Knowledge Graph**           | Create a dynamic graph of entities and relations from all inputs          |
| **🤖 Natural Language Queries**   | Use embedding-based semantic search + basic retrieval to answer questions |
| **🌐 Streamlit UI**               | Upload files, show extracted data, accept questions                       |
| **📊 Graph Visualization**        | Use `pyvis` to render interactive graphs in-browser                       |
