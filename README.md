




# AI-Powered Document Chatbot

An AI-powered document chatbot application built using FastAPI, React, LangChain, Hugging Face, and ChromaDB.
The application allows users to upload PDF/TXT documents and ask questions related to the uploaded content. The chatbot answers questions using embeddings-based retrieval and Retrieval-Augmented Generation (RAG).

---

# Features

* Upload PDF and TXT documents
* AI-powered chatbot interface
* LangChain integration
* Embeddings-based retrieval
* Chroma vector database
* Question answering from uploaded documents
* FastAPI backend
* React frontend
* Hugging Face open-source LLM integration
* RetrievalQA pipeline

---

# Tech Stack

## Frontend

* React.js
* Axios

## Backend

* FastAPI
* LangChain
* Hugging Face Transformers
* ChromaDB
* Sentence Transformers

---

# Project Structure

```bash
project/
│
├── backend/
│   ├── app.py
│   ├── uploads/
│   ├── requirements.txt
│   └── venv/
|   |__ chroma_db/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

# How It Works

1. User uploads a PDF or TXT document
2. The document is loaded and split into chunks
3. Embeddings are generated using Sentence Transformers
4. Chunks are stored in Chroma vector database
5. User asks questions through chatbot UI
6. LangChain RetrievalQA retrieves relevant chunks
7. Hugging Face LLM generates final answer based only on document content

---

# Installation and Setup

## 1. Clone Repository

```bash
git clone https://github.com/Hamna-T577/AI-chatbot
cd AI-chatbot
```

---

# Backend Setup

## 2. Navigate to Backend

```bash
cd backend
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Run Backend Server

```bash
uvicorn app:app --reload
```

Backend will run on:

```bash
http://127.0.0.1:8000
```

Swagger API Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

## 7. Navigate to Frontend

```bash
cd frontend
```

## 8. Install Dependencies

```bash
npm install
```

## 9. Start Frontend

```bash
npm run dev
```

Frontend will run on:

```bash
http://localhost:5173
```

---

# API Endpoints

## Upload Document

```http
POST /upload
```

Uploads PDF/TXT document.

---

## Chat With Document

```http
POST /chat?query=your_question
```

Returns AI-generated answer based on uploaded document.

---

# Example Questions

* What is the document about?
* What certifications are mentioned?
* What skills are listed?
* Summarize the document
* What experience does the person have?

---

# Models Used

## Embedding Model

```text
sentence-transformers/all-MiniLM-L6-v2
```

## Language Model

```text
google/flan-t5-base
```

---

# Environment Variables

Currently, no API key is required because open-source Hugging Face models are used locally.

Optional:

```env
HF_TOKEN=your_huggingface_token
```

---

# Future Improvements

* PostgreSQL integration
* Database querying through chatbot
* Chat history memory
* Multi-document support
* Authentication system
* Docker deployment

---

# Demo Video

 https://drive.google.com/file/d/1QYElJ3UM8cRVnbfmg--lBRhDStflQbPF/view?usp=sharing
https://drive.google.com/file/d/1JstDgaNTZgxD6J3GDfIMFBUcUncJmwpQ/view?usp=sharing

---

# GitHub Repository

https://github.com/Hamna-T577/AI-chatbot

---

# Author

Hamna

---

# License

This project is created for educational and internship assessment purposes.
