import os
import uuid
import boto3
import streamlit as st

st.set_page_config(page_title="Admin - Chat with PDF", layout="wide")

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings


AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
BUCKET_NAME = os.getenv("BUCKET_NAME")

EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"

if not BUCKET_NAME:
    raise ValueError("BUCKET_NAME environment variable is not set")

session = boto3.Session()
credentials = session.get_credentials()

if credentials is None:
    raise ValueError("AWS credentials not found inside container")

s3_client = session.client("s3", region_name=AWS_REGION)
bedrock_client = session.client("bedrock-runtime", region_name=AWS_REGION)

bedrock_embeddings = BedrockEmbeddings(
    model_id=EMBEDDING_MODEL_ID,
    client=bedrock_client
)


def get_unique_id() -> str:
    return str(uuid.uuid4())


def split_text(pages, chunk_size=1000, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_documents(pages)


def create_vector_store(request_id: str, documents):
    folder_path = "/tmp"
    index_name = request_id

    vectorstore_faiss = FAISS.from_documents(documents, bedrock_embeddings)
    vectorstore_faiss.save_local(folder_path=folder_path, index_name=index_name)

    faiss_path = os.path.join(folder_path, f"{index_name}.faiss")
    pkl_path = os.path.join(folder_path, f"{index_name}.pkl")

    if not os.path.exists(faiss_path):
        raise FileNotFoundError(f"FAISS file not found: {faiss_path}")

    if not os.path.exists(pkl_path):
        raise FileNotFoundError(f"PKL file not found: {pkl_path}")

    s3_client.upload_file(
        Filename=faiss_path,
        Bucket=BUCKET_NAME,
        Key=f"{request_id}.faiss"
    )

    s3_client.upload_file(
        Filename=pkl_path,
        Bucket=BUCKET_NAME,
        Key=f"{request_id}.pkl"
    )

    return faiss_path, pkl_path


def main():
    st.header("Admin Site - Chat with PDF using Bedrock + FAISS")

    st.write("Embedding model:", EMBEDDING_MODEL_ID)

    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

    if uploaded_file is not None:
        try:
            request_id = get_unique_id()
            st.write(f"Generated Request ID: `{request_id}`")

            pdf_path = f"/tmp/{request_id}.pdf"

            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            st.info("Reading PDF...")
            loader = PyPDFLoader(pdf_path)
            pages = loader.load()

            st.write(f"Total Pages: {len(pages)}")

            st.info("Splitting text into chunks...")
            split_docs = split_text(pages, chunk_size=1000, chunk_overlap=200)
            st.write(f"Total Chunks: {len(split_docs)}")

            st.info("Creating vector store and uploading to S3...")
            faiss_path, pkl_path = create_vector_store(request_id, split_docs)

            st.success("PDF processed successfully")
            st.write(f"Local FAISS file: `{faiss_path}`")
            st.write(f"Local PKL file: `{pkl_path}`")
            st.write(f"S3 FAISS key: `{request_id}.faiss`")
            st.write(f"S3 PKL key: `{request_id}.pkl`")

            st.subheader("Use this INDEX_ID in User app")
            st.code(request_id)

        except Exception as e:
            st.error(f"Error while processing PDF: {str(e)}")
            st.exception(e)


if __name__ == "__main__":
    main()