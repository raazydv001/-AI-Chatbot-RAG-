<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F7FF,50:6366F1,100:8B5CF6&height=150&section=header&text=AI%20RAG%20Chatbot&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=40"/>

### 🤖 Ask questions. Retrieve knowledge. Get grounded answers.

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge"/>
<img src="https://img.shields.io/badge/ChromaDB-7C3AED?style=for-the-badge"/>
<img src="https://img.shields.io/badge/OpenRouter-F97316?style=for-the-badge"/>

<br>

<img src="https://img.shields.io/github/stars/raazydv001/-AI-Chatbot-RAG-?style=flat-square&logo=github"/>
<img src="https://img.shields.io/github/last-commit/raazydv001/-AI-Chatbot-RAG-?style=flat-square&logo=github"/>

</div>

---

## 🧠 About

**AI RAG Chatbot** lets you chat with your own `.txt` documents using **Retrieval-Augmented Generation (RAG)**.

It retrieves relevant information from your documents, gives that context to the LLM, and generates a grounded answer.

```text
📄 Documents → ✂️ Chunks → 🧠 Embeddings → 🗄️ ChromaDB
                                             ↓
❓ Question → 🔎 Retrieval → 📚 Context → 🤖 LLM → ✅ Answer

✨ Features
Feature	Description
🤖 AI Q&A	Ask questions about your documents
🔎 Semantic Search	Retrieve information by meaning
🧠 Conversation History	Ask contextual follow-up questions
⚡ Streaming	See responses as they are generated
🗄️ ChromaDB	Local vector database
🔗 LangChain	RAG pipeline
🌐 OpenRouter	LLM and embedding API
📖 Sources	Display retrieved documents
💬 Streamlit	Interactive chat interface
🔐 .env	Secure API key management
🛠️ Tech Stack
Technology	Purpose
🐍 Python	Core programming language
🎨 Streamlit	Web application UI
🔗 LangChain	RAG orchestration
🗄️ ChromaDB	Vector database
🧠 OpenAI Embeddings	Document embeddings
🌐 OpenRouter	LLM API
🔐 python-dotenv	Environment variables
🧩 Architecture
                    📄 DOCUMENTS
                         │
                         ▼
                ┌─────────────────┐
                │ Document Loader │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  Text Splitter  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Embeddings    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    ChromaDB     │
                └────────┬────────┘
                         │
                         │
                  ❓ User Question
                         │
                         ▼
                ┌─────────────────┐
                │    Retriever    │
                └────────┬────────┘
                         │
                         ▼
                  📚 Relevant Chunks
                         │
                         ▼
                ┌─────────────────┐
                │       LLM       │
                └────────┬────────┘
                         │
                         ▼
                  ✅ Grounded Answer

Getting Started
Prerequisites
Python 3.9+
An OpenRouter API key
1. Clone and install
bash
git clone https://github.com/raazydv001/-AI-Chatbot-RAG-.git
cd ./-AI-Chatbot-RAG-

python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

pip install -r requirements.txt
2. Configure environment

Create a .env file in the project root:

env
OPENROUTER_API_KEY=your_openrouter_api_key_here

Never commit your real API key. Make sure .env is listed in .gitignore.

3. Add your documents

Place your .txt files in the docs/ folder:

text
docs/
├── company.txt
├── product.txt
└── notes.txt
4. Build the index and run
bash
python ingest.py        # build the vector database
streamlit run app.py    # start the chatbot

Re-run python ingest.py whenever your documents change.

Project Structure
text
.
├── app.py              # Streamlit chat interface
├── ingest.py           # Builds the ChromaDB vector store
├── docs/               # Your .txt source documents
├── requirements.txt    # Python dependencies
└── .env                # API key (not committed)
