import os

from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_openai import (
    OpenAIEmbeddings,
    ChatOpenAI
)


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

CHROMA_FOLDER = "./chroma_db"


# ============================================================
# EMBEDDING MODEL
# ============================================================

embeddings = OpenAIEmbeddings(
    model="openai/text-embedding-3-small",
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


# ============================================================
# CHROMA DATABASE
# ============================================================

db = Chroma(
    persist_directory=CHROMA_FOLDER,
    embedding_function=embeddings
)


# ============================================================
# RETRIEVER
# ============================================================

retriever = db.as_retriever(
    search_kwargs={
        "k": 4
    }
)


# ============================================================
# LLM
# ============================================================

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.2,
    streaming=True
)


# ============================================================
# RETRIEVE DOCUMENTS
# ============================================================

def retrieve_documents(question):

    documents = retriever.invoke(question)

    return documents


# ============================================================
# CREATE PROMPT MESSAGES
# ============================================================

def create_messages(question, history, documents):

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    messages = [

        (
            "system",
            f"""
You are a helpful AI RAG chatbot.

You answer using two sources:

1. Conversation history
2. Retrieved documents

========================
CONVERSATION HISTORY
========================

{format_history(history)}

========================
RETRIEVED DOCUMENTS
========================

{context}

========================
RULES
========================

1. Use conversation history when the user refers to
   something previously discussed.

2. Use retrieved documents for questions about the
   information contained in the documents.

3. Do not invent facts that are not available in the
   conversation history or retrieved documents.

4. If the answer is not available in either source,
   say:

   "I don't know based on the available information."

5. Answer naturally and clearly.

6. Keep the answer reasonably concise.
"""
        ),

    ]

    # Add conversation history
    for message in history:

        messages.append(
            (
                message["role"],
                message["content"]
            )
        )

    # Add current question
    messages.append(
        (
            "user",
            question
        )
    )

    return messages


# ============================================================
# FORMAT HISTORY
# ============================================================

def format_history(history):

    if not history:
        return "No previous conversation."

    history_text = ""

    for message in history:

        role = message["role"].capitalize()

        history_text += (
            f"{role}: "
            f"{message['content']}\n"
        )

    return history_text


# ============================================================
# STREAM ANSWER
# ============================================================

def stream_answer(question, history):

    documents = retrieve_documents(question)

    messages = create_messages(
        question,
        history,
        documents
    )

    for chunk in llm.stream(messages):

        if chunk.content:

            yield chunk.content


# ============================================================
# GET SOURCES
# ============================================================

def get_sources(question):

    documents = retrieve_documents(question)

    sources = []

    for document in documents:

        source = document.metadata.get("source")

        if source and source not in sources:

            sources.append(source)

    return sources