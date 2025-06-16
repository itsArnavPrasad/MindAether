# Task Breakdown
## 1. UI Layer
### 1.1 Streamlit UI
 - Build upload interface for files (text, images)

 - Add query input box (text box)

 - Display answers (chat-style, table)

 - Show iframe for graph visualization

 - Enable basic routing: Upload → Ingest, Query → Search

### 1.2 CLI with Typer
 - Set up CLI using Typer

 - Add commands: ingest, query, reset, status

 - Wire CLI functions to ingestion & search pipeline

## 2. Ingestion Layer
### 2.1 File Router
 - Detect MIME/type (text, image, unsupported)

 - Route file to correct parser

### 2.2 Text Parser
 - Extract text from .pdf (e.g., pdfminer, PyMuPDF)

 - Extract text from .docx and .txt

 - Return clean string to next module

### 2.3 Image OCR + Embeddings
 - Apply Tesseract OCR to image files

 - Extract visual embeddings with CLIP

 - Return text + embeddings to Extraction Layer

## 3. Extraction Layer
### 3.1 Text Normalizer
 - Clean unwanted characters, handle encodings

 - Split into paragraphs/sentences/tokens

### 3.2 NER & Relation Extraction
 - Use spaCy for entity recognition

 - Optional : Integrate a local finetuned LLM
 
 - Extract subject-relation-object triples for graph

### 3.3 Metadata Extractor
 - Extract timestamps, EXIF (for image files)

 - Attach metadata as tags to content nodes

## 4. Graph Layer
### 4.1 Graph Builder
 - Use networkx to build entity-relation graph

 - Add node metadata and relationships

 - Deduplicate similar nodes

### 4.2 Graph Serializer
 - Export/import graph as .json or .graphml

 - Save each session into a graph file

### 4.3 Embedding Store
 - Generate sentence/document embeddings

 - Store them in memory (initially), then file/db

## 5. Query Layer
### 5.1 Semantic Search Engine
 - Implement FAISS or cosine similarity search

 - Search embeddings for similar content

### 5.2 LLM Retriever
 - (Optional) Use llama-cpp or OpenAI to summarize matches

 - Give a fallback if no good result is found

### 5.3 Answer Synthesizer
 - Format response: text/table with source snippet

 - Score or rank results if multiple matches

## 6. Visualization Layer
### 6.1 Graph Visualizer
 - Use pyvis to render graph

 - Make it interactive (hover = metadata, click = zoom)

### 6.2 Streamlit Components
 - Embed iframe for pyvis

 - Add display for tables (entities, files)

 - Toggle between visual and textual answers

