# InsightRAG – RAG System with AWS Bedrock

## 📌 Overview
InsightRAG is a full-stack Retrieval-Augmented Generation (RAG) system that enables intelligent querying of PDF documents using AWS Bedrock, FAISS, and LLMs.

This project is divided into two main components:
- **Admin Module** → Document ingestion & indexing
- **User Module** → Querying & conversational AI

---

## 🏗️ Architecture Summary

### 🔹 Admin Pipeline (Ingestion)
1. Upload PDF
2. Extract text
3. Chunk documents
4. Generate embeddings (Amazon Titan)
5. Store in FAISS vector DB
6. Upload index to AWS S3
7. Generate `INDEX_ID`

### 🔹 User Pipeline (Retrieval)
1. Enter query + INDEX_ID
2. Download FAISS index from S3
3. Embed query (Titan)
4. Perform similarity search (Top-K)
5. Build prompt with context
6. Generate response using Claude 3 (Bedrock)
7. Display answer + source chunks

---

## 📁 Project Structure

```
.
├── Admin/
│   ├── Admin.py
│   ├── requirements.txt
│   ├── Dockerfile
│
├── User/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│
├── README.md
```

---

## 🧰 Tech Stack

### 🔹 Backend
- Python
- LangChain

### 🔹 Frontend
- Streamlit

### 🔹 AI / ML
- Amazon Titan (Embeddings)
- Claude 3 Haiku (LLM via AWS Bedrock)

### 🔹 Vector Store
- FAISS

### 🔹 Cloud
- AWS S3 (Index storage)
- AWS IAM (Security)
- AWS Bedrock (LLM + embeddings)

### 🔹 DevOps
- Docker
- GitHub Actions (CI/CD ready)

---

## ⚙️ Setup Instructions

### 1. Clone Repo
```bash
git clone <repo-url>
cd InsightRAG
```

---

### 2. Install Dependencies

#### Admin
```bash
cd Admin
pip install -r requirements.txt
```

#### User
```bash
cd ../User
pip install -r requirements.txt
```

---

### 3. Configure AWS
```bash
aws configure
```

Set:
- AWS Access Key
- AWS Secret Key
- Region

---

## ▶️ Running the Application

### 🔹 Run Admin App
```bash
cd Admin
streamlit run Admin.py
```

👉 Upload PDF → Generate INDEX_ID

---

### 🔹 Run User App
```bash
cd User
streamlit run app.py
```

👉 Enter INDEX_ID → Ask questions

---

## 🐳 Docker Support

### Admin
```bash
cd Admin
docker build -t insightrag-admin .
docker run -p 8501:8501 insightrag-admin
```

### User
```bash
cd User
docker build -t insightrag-user .
docker run -p 8502:8501 insightrag-user
```

---

## 🔄 CI/CD Pipeline

Pipeline flow:

```
GitHub Push
   ↓
GitHub Actions
   ↓
Install Dependencies
   ↓
Build Docker Image
   ↓
Deploy to AWS (EC2 / ECS)
```

---

## 🔐 Security & Monitoring
- IAM roles for secure AWS access
- S3 for scalable storage
- CloudWatch (optional) for monitoring

---

## 🚀 Features
- End-to-end RAG system
- Real-time document Q&A
- Source-aware answers
- Scalable cloud architecture
- Modular design (Admin + User separation)

---

## 💼 Use Cases
- Financial document analysis
- Legal document search
- Research assistant
- Enterprise knowledge base

---

## 👨‍💻 Author
Komal Wavhal  
AI/ML Engineer | Ex-JPMorgan Chase

---

## ⭐ Support
If you found this useful, give it a ⭐ on GitHub!
