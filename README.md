<div align="center">

# 🤖 AI RAG Chatbot

### Ask questions. Retrieve knowledge. Get grounded answers.

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&pause=1000&color=00F7FF&center=true&vCenter=true&width=700&lines=AI+RAG+Chatbot;Retrieval+Augmented+Generation;LangChain+%7C+ChromaDB+%7C+OpenRouter;Context-Aware+AI+Conversations" />
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/ChromaDB-Vector_DB-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenRouter-LLM-orange?style=for-the-badge">
</p>

</div>

---

## 🧠 About

AI RAG Chatbot is a Retrieval-Augmented Generation application that allows users to ask questions about a collection of documents.

Instead of relying only on the knowledge stored inside an LLM, the application retrieves relevant information from a local vector database and provides that context to the LLM before generating the answer.

### 🔥 What it does

```text
Documents
    ↓
Load
    ↓
Split into chunks
    ↓
Generate embeddings
    ↓
Store in ChromaDB
    ↓
User Question
    ↓
Similarity Search
    ↓
Relevant Documents
    ↓
LLM
    ↓
Grounded Answer
