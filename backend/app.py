
# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware

# from langchain_community.document_loaders import PyPDFLoader, TextLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# from langchain.chains import RetrievalQA
# from langchain_community.embeddings import HuggingFaceEmbeddings

# from langchain_google_genai import ChatGoogleGenerativeAI

# import shutil
# import os
# from dotenv import load_dotenv

# load_dotenv()

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# qa_chain = None


# @app.get("/")
# def home():
#     return {"message": "Backend Running"}


# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     global qa_chain

#     # os.makedirs("uploads", exist_ok=True)
#     if not os.path.exists("uploads"):
#         os.mkdir("uploads")

#     file_path = f"uploads/{file.filename}"

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     # LOAD DOCUMENT
#     if file.filename.endswith(".pdf"):
#         loader = PyPDFLoader(file_path)
#     else:
#         loader = TextLoader(file_path)

#     documents = loader.load()

#     print("Document Loaded")

#     # SPLIT TEXT
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200
#     )

#     docs = text_splitter.split_documents(documents)

#     print("Text Split Done")

#     # EMBEDDINGS
#     embeddings = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )

#     print("Embeddings Ready")

#     # VECTOR STORE
#     # vectorstore = Chroma.from_documents(
#     #     docs,
#     #     embeddings,
#     #     persist_directory="chroma_db"
#     # )
    
# # CREATE chroma_db FOLDER
#     if not os.path.exists("chroma_db"):
#         os.mkdir("chroma_db")

# # VECTOR STORE
#     vectorstore = Chroma.from_documents(
#         docs,
#         embeddings,
#         persist_directory="./chroma_db"
#         )



#     retriever = vectorstore.as_retriever()

#     # GEMINI MODEL
#     llm = ChatGoogleGenerativeAI(
#         model="gemini-1.5-flash",
#         temperature=0,
#         google_api_key=GOOGLE_API_KEY,
#         convert_system_message_to_human=True
#     )

#     # QA CHAIN
#     qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=retriever
#     )

#     return {"message": "File uploaded successfully"}


# @app.post("/chat")
# async def chat(query: str):

#     global qa_chain

#     if qa_chain is None:
#         return {"answer": "Please upload a document first."}

#     prompt = f"""
#     Answer ONLY from the uploaded document context.
    
#     If answer is not available in the document, say:
#     'I could not find this in the uploaded document.'

#     Question:
#     {query}

#     """

#     # response = qa_chain.run(prompt)
#     response = qa_chain.invoke(prompt)

#     return {"answer": response["result"]}










# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware

# from langchain_community.document_loaders import PyPDFLoader, TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma

# from langchain.chains import RetrievalQA
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.llms import HuggingFacePipeline

# from transformers import pipeline

# import shutil
# import os

# # ----------------------------
# # APP INIT
# # ----------------------------
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# qa_chain = None


# # ----------------------------
# # HOME ROUTE
# # ----------------------------
# @app.get("/")
# def home():
#     return {"message": "Chatbot Backend Running 🚀"}


# # ----------------------------
# # UPLOAD DOCUMENT
# # ----------------------------
# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     global qa_chain

#     # create folder
#     os.makedirs("uploads", exist_ok=True)

#     file_path = f"uploads/{file.filename}"

#     # save file
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     # ----------------------------
#     # LOAD DOCUMENT
#     # ----------------------------
#     if file.filename.endswith(".pdf"):
#         loader = PyPDFLoader(file_path)
#     else:
#         loader = TextLoader(file_path)

#     documents = loader.load()
#     print("Document Loaded")

#     # ----------------------------
#     # SPLIT TEXT
#     # ----------------------------
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200
#     )

#     docs = splitter.split_documents(documents)
#     print("Text Split Done")

#     # ----------------------------
#     # EMBEDDINGS
#     # ----------------------------
#     embeddings = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )
#     print("Embeddings Ready")

#     # ----------------------------
#     # VECTOR DB
#     # ----------------------------
#     vectorstore = Chroma.from_documents(
#         docs,
#         embeddings,
#         persist_directory="./chroma_db"
#     )

#     retriever = vectorstore.as_retriever()

#     # ----------------------------
#     # FREE LLM (NO API KEY)
#     # ----------------------------
#     pipe = pipeline(
#         "text-generation",
#         model="distilgpt2",
#         max_new_tokens=256
#     )

#     llm = HuggingFacePipeline(pipeline=pipe)

#     # ----------------------------
#     # QA CHAIN
#     # ----------------------------
#     qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=retriever
#     )

#     return {"message": "File uploaded and chatbot is ready ✅"}


# # ----------------------------
# # CHAT ENDPOINT
# # ----------------------------
# @app.post("/chat")
# async def chat(query: str):
#     global qa_chain

#     if qa_chain is None:
#         return {"answer": "Please upload a document first."}

#     try:
#         response = qa_chain.invoke(query)
#         return {"answer": response["result"]}

#     except Exception as e:
#         return {"answer": f"Error: {str(e)}"}








from fastapi import FastAPI, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware

import os
import shutil

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline

from langchain.chains import RetrievalQA
from transformers import pipeline

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

qa_chain = None


@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global qa_chain

    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Load document
    if file.filename.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)

    documents = loader.load()

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = splitter.split_documents(documents)

    # Embeddings (FREE)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Vector DB
    vectorstore = Chroma.from_documents(
        docs,
        embeddings
    )

    retriever = vectorstore.as_retriever()

    # FREE LLM (NO QUOTA)
#     pipe = pipeline(
#     "text-generation",
#     model="distilgpt2",
#     max_new_tokens=100
# )
    pipe = pipeline(
    "text-generation",
    model="distilgpt2",
    max_new_tokens=100
    )


    llm = HuggingFacePipeline(pipeline=pipe)

    # QA Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

    return {"message": "File uploaded successfully"}


@app.post("/chat")
async def chat(query: str = Query(...)):
    global qa_chain

    if qa_chain is None:
        return {"answer": "Please upload a document first."}

    response = qa_chain.invoke({"query": query})

    return {"answer": response["result"]}