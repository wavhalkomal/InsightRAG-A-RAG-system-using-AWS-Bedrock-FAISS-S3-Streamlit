# 🚀 InsightRAG – AI-Powered Document Intelligence (RAG System)

## 📌 Overview

InsightRAG is a production-ready Retrieval-Augmented Generation (RAG) system that transforms unstructured PDF documents into an intelligent, queryable knowledge base using AWS Bedrock, FAISS, and Large Language Models.

The system enables users to upload documents, generate embeddings, and interact with them using natural language queries while ensuring responses are grounded in document context with source transparency.

---

## 🎯 Key Features

- Upload and process PDF documents  
- Generate embeddings using Amazon Titan (AWS Bedrock)  
- High-performance vector similarity search using FAISS  
- Store vector indexes in AWS S3  
- Context-aware Q&A using Claude 3 Haiku (Bedrock)  
- Retrieval-Augmented Generation (RAG)  
- Source chunk display for explainability  
- Secure access via AWS IAM  
- Monitoring via CloudWatch  
- CI/CD pipeline using GitHub Actions + Docker  

---

## 🏗️ System Architecture

### Admin App (Ingestion Pipeline)

PDF Upload → Text Extraction → Chunking → Embeddings (Amazon Titan) → FAISS → Upload to S3 → INDEX_ID

### User App (Retrieval Pipeline)

User Query → INDEX_ID → Load FAISS → Query Embedding → Similarity Search → Prompt Builder → Claude 3 → Answer + Sources

---

## 🧰 Tech Stack

**Frontend:** Streamlit  
**Backend:** Python, LangChain  
**AI/ML:** Amazon Titan, Claude 3 Haiku (AWS Bedrock)  
**Vector DB:** FAISS  
**Cloud:** AWS S3, IAM, CloudWatch  
**DevOps:** Docker, GitHub Actions  

---

## 📁 Project Structure

.
├── Admin.py  
├── app.py  
├── requirements.txt  
├── Dockerfile  

---

## ⚙️ Setup Instructions

```bash
git clone <your-repo-url>
cd insight-rag
pip install -r requirements.txt
```

Configure AWS:

```bash
aws configure
```

---

## ▶️ Run Application

```bash
streamlit run Admin.py
streamlit run app.py
```

---

## 🔄 CI/CD Pipeline

GitHub Actions → Build Docker → Deploy to AWS

---

## 🐳 Docker

```bash
docker build -t insight-rag .
docker run -p 8501:8501 insight-rag
```

---

## 👨‍💻 Author

Komal Wavhal  
AI/ML Engineer | Ex-JPMorgan Chase
