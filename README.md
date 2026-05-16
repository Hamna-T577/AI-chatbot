````markdown
# AI Document Chatbot

An AI-powered chatbot application that allows users to upload PDF/TXT documents and ask questions related to the uploaded content.

---

# Features

- Upload PDF or TXT files
- AI-based question answering
- Embeddings-based retrieval
- ChromaDB vector storage
- LangChain integration
- React frontend UI
- FastAPI backend

---

# Technologies Used

## Frontend
- React JS
- Tailwind CSS
- Axios

## Backend
- FastAPI
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Google Gemini API

---

# Project Structure

ai-document-chatbot/

├── backend/

├── frontend/

└── README.md

---

# Setup Instructions

## Backend Setup

### Step 1
Go to backend folder:

```bash
cd backend
````

### Step 2

Create virtual environment:

```bash
python -m venv venv
```

### Step 3

Activate virtual environment:

```bash
venv\Scripts\activate
```

### Step 4

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 5

Create .env file:

```env
GOOGLE_API_KEY=your_google_api_key
```

### Step 6

Run backend:

```bash
uvicorn app:app --reload
```

Backend runs on:

http://127.0.0.1:8000

---

# Frontend Setup

### Step 1

Go to frontend folder:

```bash
cd frontend
```

### Step 2

Install dependencies:

```bash
npm install
```

### Step 3

Run frontend:

```bash
npm run dev
```

Frontend runs on:

http://localhost:5173

---

# Workflow

1. User uploads document
2. Backend processes document
3. Text is split into chunks
4. Embeddings are created
5. ChromaDB stores embeddings
6. User asks question
7. Relevant chunks retrieved
8. Gemini generates answer

---

# Future Improvements

* PostgreSQL integration
* Chat history storage
* User authentication
* Multi-document support
* Streaming AI responses

---

# Author

Hamna

```
```
