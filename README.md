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

Replace your current section with this:

## 🚀 Run With Your Own Documents

### 1️⃣ Clone & Install

```bash
git clone https://github.com/raazydv001/-AI-Chatbot-RAG-.git
cd ./-AI-Chatbot-RAG-
python -m venv venv

Windows

venv\Scripts\activate

macOS / Linux

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
2️⃣ Add Your API Key

Create .env in the project root:

OPENROUTER_API_KEY=your_openrouter_api_key_here

⚠️ Never commit your real API key to GitHub.

3️⃣ Add Your Documents

Put your own .txt files inside docs/:

docs/
├── company.txt
├── product.txt
└── notes.txt
4️⃣ Build & Run

Create the vector database:

python ingest.py

Start the chatbot:

streamlit run app.py

🔄 Run python ingest.py again whenever your documents change.

🧪 Quick Workflow
🚀 Clone Repository
        ↓
📦 Install Dependencies
        ↓
🔑 Add OpenRouter API Key
        ↓
📚 Add Your .txt Documents
        ↓
🗄️ Run python ingest.py
        ↓
▶️ Run streamlit run app.py
        ↓
💬 Ask Questions
        ↓
🤖 Get Grounded Answers
🔮 Future Improvements
Improvement	Status
📄 PDF Support	🔜 Planned
📝 DOCX Support	🔜 Planned
✂️ Better Chunking	🔜 Planned
🔀 Hybrid Search	🔜 Planned
🎯 Reranking	🔜 Planned
🏷️ Metadata Filtering	🔜 Planned
📚 Better Citations	🔜 Planned
🔐 Authentication	🔜 Planned
☁️ Cloud Deployment	🔜 Planned
💾 Persistent Chat History	🔜 Planned
📊 RAG Evaluation	🔜 Planned
👨‍💻 Author
<div align="center">
Raj Yadav

B.Tech Computer Science Engineering

🤖 AI Engineering · 🧠 Generative AI · 🔎 RAG · ☁️ Cloud Computing · 💻 Software Engineering

<br><br>

⭐ If you found this project useful, consider giving it a star!

</div>
<div align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:8B5CF6,50:6366F1,100:00F7FF&height=100&section=footer"/>

Built with ❤️ using Python · LangChain · ChromaDB · Streamlit · OpenRouter

</div> ```
