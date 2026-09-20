<div align="center">

# 🤖 AI RAG Chatbot

### Ask questions. Retrieve knowledge. Get grounded answers.

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&pause=1000&color=00F7FF&center=true&vCenter=true&width=700&lines=AI+RAG+Chatbot;Retrieval+Augmented+Generation;LangChain+%7C+ChromaDB+%7C+OpenRouter;Context-Aware+AI+Conversations" />

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

AI RAG Chatbot is a Retrieval-Augmented Generation app that lets you ask questions about your own documents.

It retrieves relevant information from your documents using **ChromaDB** and sends that context to an **LLM** to generate grounded answers.

### 🔥 RAG Flow

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
Relevant Chunks
   ↓
LLM
   ↓
Grounded Answer



✨ Features
🤖 AI document Q&A
📚 Retrieval-Augmented Generation
🔎 Semantic search
🧠 Conversation history
⚡ Streaming responses
🗄️ ChromaDB vector database
🔗 LangChain
🌐 OpenRouter API
📖 Source display
💬 Streamlit chat UI
🔐 Secure .env API key
🛠️ Tech Stack
Technology	Purpose
Python	Core language
Streamlit	UI
LangChain	RAG
ChromaDB	Vector database
OpenAI Embeddings	Embeddings
OpenRouter	LLM API
python-dotenv	Environment variables
🧩 Architecture
                ┌───────────────┐
                │   Documents   │
                └───────┬───────┘
                        ↓
                ┌───────────────┐
                │ Document Load │
                └───────┬───────┘
                        ↓
                ┌───────────────┐
                │ Text Splitter │
                └───────┬───────┘
                        ↓
                ┌───────────────┐
                │  Embeddings   │
                └───────┬───────┘
                        ↓
                ┌───────────────┐
                │   ChromaDB    │
                └───────┬───────┘
                        ↓
                  User Question
                        ↓
                ┌───────────────┐
                │   Retriever   │
                └───────┬───────┘
                        ↓
                Relevant Chunks
                        ↓
                ┌───────────────┐
                │      LLM      │
                └───────┬───────┘
                        ↓
                Grounded Answer
⚙️ How It Works

1. Load Documents
Reads .txt files from the docs/ folder.

2. Split Documents
Large documents are divided into smaller chunks.

3. Generate Embeddings
Each chunk is converted into a vector representing its meaning.

4. Store in ChromaDB
The vectors are stored locally.

5. Ask a Question
Example:

What products does Microsoft offer?

6. Retrieve Relevant Information
The question is compared with document embeddings and the most relevant chunks are retrieved.

7. Generate Answer
The retrieved context is sent to the LLM to generate the response.

🚀 Use This Project With Your Own Documents

You can use this project with your own OpenRouter API key and your own .txt files.

1️⃣ Clone
git clone https://github.com/raazydv001/-AI-Chatbot-RAG-.git
cd ./-AI-Chatbot-RAG-
2️⃣ Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

macOS / Linux

python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt

Or:

pip install streamlit langchain langchain-community langchain-text-splitters langchain-openai langchain-chroma python-dotenv
🔑 Add Your Own API Key

Create a .env file in the project root:

OPENROUTER_API_KEY=your_openrouter_api_key_here

Never upload your real API key to GitHub.

The .gitignore already excludes:

.env
venv/
chroma_db/
__pycache__/
📚 Add Your Own Documents

Put your own .txt files inside docs/.

Example:

docs/
├── company.txt
├── product.txt
├── research.txt
└── notes.txt

Example:

docs/python_notes.txt
Python is a high-level programming language.
It is widely used for web development,
automation, data science and artificial intelligence.

Then you can ask:

What is Python used for?
🗄️ Create the Vector Database

After adding or changing documents:

python ingest.py

Pipeline:

Documents
   ↓
Load
   ↓
Split
   ↓
Embeddings
   ↓
ChromaDB

This creates the local chroma_db/ directory.

Run python ingest.py again whenever your documents change.

▶️ Start the Chatbot
streamlit run app.py

Then open the local URL shown by Streamlit.

💬 Example Questions
Tell me about Google.

What products does Microsoft offer?

What does NVIDIA do?

Tell me about Tesla.

Compare Google and Microsoft.

What information is available in my resume?

You can also ask follow-up questions because conversation history is maintained during the session.

📁 Project Structure
AI-Chatbot-RAG/
│
├── assets/
│   └── demo.gif
│
├── docs/
│   ├── Google.txt
│   ├── Meta.txt
│   ├── Microsoft.txt
│   ├── NVIDIA.txt
│   ├── Tesla.txt
│   └── resume.txt
│
├── app.py
├── ingest.py
├── rag.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
Files

app.py → Streamlit UI, chat, history, streaming, sources

ingest.py → Loads, splits, embeds and stores documents

rag.py → Retrieval, prompt creation, LLM calls and sources

docs/ → Your knowledge base

chroma_db/ → Local vector database

🔐 Security

Use .env for your API key:

OPENROUTER_API_KEY=your_api_key_here

Never hard-code secrets:

API_KEY = "sk-xxxxxxxxxxxxxxxx"

Never commit API keys to GitHub.

🧪 Quick Workflow
Clone
 ↓
Install dependencies
 ↓
Add OpenRouter API key
 ↓
Add your .txt documents
 ↓
Run python ingest.py
 ↓
Run streamlit run app.py
 ↓
Ask questions
🌟 Why RAG?
Traditional LLM
Question
   ↓
  LLM
   ↓
Answer
RAG
Question
   ↓
Retrieve Knowledge
   ↓
Relevant Documents
   ↓
LLM
   ↓
Grounded Answer

RAG gives the LLM relevant external information at query time instead of relying only on its pretrained knowledge.

🔮 Future Improvements
 PDF support
 DOCX support
 Better chunking
 Hybrid search
 Reranking
 Metadata filtering
 Better citations
 Authentication
 Cloud deployment
 Persistent chat history
 RAG evaluation
👨‍💻 Author
Raj Yadav

B.Tech Computer Science Engineering

🤖 AI Engineering | 🧠 Generative AI | 🔎 RAG | ☁️ Cloud | 💻 Software Engineering

<div align="center">
⭐ If you found this project useful, consider giving it a star!

Built with ❤️ using Python, LangChain, ChromaDB, Streamlit & OpenRouter

</div> ```

After saving README.md, run:

git add README.md
git commit -m "Improve project README"
git push
