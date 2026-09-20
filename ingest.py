import os
import shutil
from pathlib import Path

from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError(
        "OPENROUTER_API_KEY not found. Check your .env file."
    )


# ============================================================
# CONFIGURATION
# ============================================================

DOCS_FOLDER = "docs"
CHROMA_FOLDER = "./chroma_db"

# True = delete old database before ingestion
RESET_DATABASE = True


# ============================================================
# LOAD DOCUMENTS
# ============================================================

def load_documents():

    documents = []

    docs_path = Path(DOCS_FOLDER)

    if not docs_path.exists():
        raise FileNotFoundError(
            f"'{DOCS_FOLDER}' folder not found."
        )

    txt_files = list(docs_path.glob("*.txt"))

    if not txt_files:
        raise FileNotFoundError(
            "No .txt files found inside the docs folder."
        )

    for file_path in txt_files:

        loader = TextLoader(
            str(file_path),
            encoding="utf-8"
        )

        docs = loader.load()

        documents.extend(docs)

    return documents


# ============================================================
# SPLIT DOCUMENTS
# ============================================================

def split_documents(documents):

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    return chunks


# ============================================================
# CREATE EMBEDDING MODEL
# ============================================================

def create_embeddings():

    embeddings = OpenAIEmbeddings(
        model="openai/text-embedding-3-small",
        api_key=API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )

    return embeddings


# ============================================================
# STORE IN CHROMA
# ============================================================

def create_vector_database(chunks, embeddings):

    if RESET_DATABASE and os.path.exists(CHROMA_FOLDER):

        print("Removing old Chroma database...")

        shutil.rmtree(CHROMA_FOLDER)

    print("Creating Chroma vector database...")

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_FOLDER
    )

    return vector_db


# ============================================================
# MAIN
# ============================================================

def main():

    print("\n========================================")
    print("      RAG INGESTION STARTED")
    print("========================================")

    # Load
    documents = load_documents()

    print(f"\nDocuments loaded: {len(documents)}")

    for doc in documents:
        print(
            "Source:",
            doc.metadata.get("source")
        )

    # Split
    chunks = split_documents(documents)

    print(f"\nChunks created: {len(chunks)}")

    # Embeddings
    embeddings = create_embeddings()

    print("\nEmbedding model created.")

    # Chroma
    create_vector_database(
        chunks,
        embeddings
    )

    print("\n========================================")
    print("     CHROMA DATABASE CREATED")
    print("========================================")

    print("\nStored inside:")
    print(CHROMA_FOLDER)

    print("\nIngestion completed successfully.")


if __name__ == "__main__":
    main()