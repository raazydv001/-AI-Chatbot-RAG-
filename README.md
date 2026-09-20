<!-- ========================= HEADER ========================= -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F7FF,50:6366F1,100:8B5CF6&height=180&section=header&text=AI%20RAG%20Chatbot&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=40"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=23&pause=1000&color=00F7FF&center=true&vCenter=true&width=800&lines=Ask+questions.+Retrieve+knowledge.+Get+grounded+answers.;Retrieval+Augmented+Generation;LangChain+%7C+ChromaDB+%7C+OpenRouter;Context-Aware+AI+Conversations" />

<br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white"/>
<img src="https://img.shields.io/badge/ChromaDB-Vector_DB-7C3AED?style=for-the-badge"/>
<img src="https://img.shields.io/badge/OpenRouter-LLM-F97316?style=for-the-badge"/>

<br><br>

<img src="https://img.shields.io/github/stars/raazydv001/-AI-Chatbot-RAG-?style=flat-square&logo=github"/>
<img src="https://img.shields.io/github/forks/raazydv001/-AI-Chatbot-RAG-?style=flat-square&logo=github"/>
<img src="https://img.shields.io/github/last-commit/raazydv001/-AI-Chatbot-RAG-?style=flat-square&logo=github"/>

</div>

---

# 🧠 About

**AI RAG Chatbot** is a Retrieval-Augmented Generation application that allows you to chat with your own documents.

Instead of relying only on an LLM's pretrained knowledge, the application:

> 📚 **Retrieves relevant information → gives it to the LLM → generates a grounded answer**

### ⚡ RAG Flow

```text
             📄 YOUR DOCUMENTS
                    │
                    ▼
             📥 Document Loader
                    │
                    ▼
              ✂️ Text Splitting
                    │
                    ▼
            🧠 Generate Embeddings
                    │
                    ▼
             🗄️ ChromaDB
                    │
                    │
              ❓ User Question
                    │
                    ▼
              🔎 Similarity Search
                    │
                    ▼
             📚 Relevant Chunks
                    │
                    ▼
                 🤖 LLM
                    │
                    ▼
             ✅ Grounded Answer


             ✨ Features
<div align="center">
🚀 Feature	💡 Description
🤖 AI Document Q&A	Ask questions about your documents
📚 RAG	Retrieves relevant knowledge before answering
🔎 Semantic Search	Finds information based on meaning
🧠 Conversation History	Supports contextual follow-up questions
⚡ Streaming	Responses appear progressively
🗄️ ChromaDB	Local vector database
🔗 LangChain	RAG pipeline orchestration
🌐 OpenRouter	LLM and embedding API
📖 Sources	Displays retrieved source documents
💬 Streamlit	Interactive chat interface
🔐 .env	Keeps API keys outside the code

🛠️ Tech Stack
<div align="center">
Technology	Purpose
🐍 Python	Core programming language
🎨 Streamlit	Web application UI
🔗 LangChain	RAG orchestration
🗄️ ChromaDB	Vector database
🧠 OpenAI Embeddings	Document embeddings
🌐 OpenRouter	LLM API
🔐 python-dotenv	Environment variables
</div>

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
                     │  Text Splitter │
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
                     │ Vector Database │
                     └────────┬────────┘
                              │
                              │
                       ❓ USER QUESTION
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
                     ✅ GROUNDED ANSWER
⚙️ How It Works
1️⃣ Load Documents

The application reads .txt files from the docs/ folder.

docs/
├── Google.txt
├── Meta.txt
├── Microsoft.txt
├── NVIDIA.txt
└── Tesla.txt
2️⃣ Split Documents

Large documents are divided into smaller chunks so relevant information can be retrieved efficiently.

3️⃣ Generate Embeddings

Each chunk is converted into a vector representing its semantic meaning.

4️⃣ Store in ChromaDB

The generated vectors are stored locally in ChromaDB.

Document Chunk
      ↓
Embedding
      ↓
ChromaDB
5️⃣ User Asks a Question

Example:

❓ What products does Microsoft offer?
6️⃣ Retrieve Relevant Information

The question is converted into an embedding and compared with stored embeddings.

The most relevant chunks are retrieved.

7️⃣ Generate Answer

The retrieved context is provided to the LLM together with the question.

The LLM then generates the final grounded response.

🚀 Use This Project With Your Own Documents

You can clone this project and use it with:

🔑 Your own OpenRouter API key
📚 Your own .txt documents

1️⃣ Clone the Repository
git clone https://github.com/raazydv001/-AI-Chatbot-RAG-.git
cd ./-AI-Chatbot-RAG-
2️⃣ Create a Virtual Environment
🪟 Windows
python -m venv venv
venv\Scripts\activate
🐧 macOS / Linux
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt

Or install manually:

pip install streamlit langchain langchain-community langchain-text-splitters langchain-openai langchain-chroma python-dotenv
🔑 4️⃣ Add Your Own OpenRouter API Key

Create a .env file in the project root:

OPENROUTER_API_KEY=your_openrouter_api_key_here

Example project location:

AI-Chatbot-RAG/
│
├── .env
├── app.py
├── ingest.py
├── rag.py
└── ...
⚠️ Important

Never upload your real API key to GitHub.

The project already ignores:

.env
venv/
chroma_db/
__pycache__/
📚 5️⃣ Add Your Own Documents

Put your own .txt files inside docs/.

Example:

docs/
├── company.txt
├── product.txt
├── research.txt
└── notes.txt

For example:

docs/python_notes.txt

Content:

Python is a high-level programming language.
It is widely used for web development,
automation, data science and artificial intelligence.

Now you can ask:

❓ What is Python used for?

The chatbot retrieves the relevant information from your documents.

🗄️ 6️⃣ Create the Vector Database

After adding or changing your documents:

python ingest.py

The ingestion pipeline:

📄 Documents
     ↓
📥 Load
     ↓
✂️ Split
     ↓
🧠 Embeddings
     ↓
🗄️ ChromaDB

This creates:

chroma_db/

Run python ingest.py again whenever your documents change.

▶️ 7️⃣ Start the Chatbot
streamlit run app.py

Then open the local URL shown by Streamlit.

🎉 Your RAG chatbot is ready!

💬 Example Questions

Try questions based on your documents:

❓ Tell me about Google.

❓ What products does Microsoft offer?

❓ What does NVIDIA do?

❓ Tell me about Tesla.

❓ Compare Google and Microsoft.

❓ What information is available in my resume?

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



🧪 Quick Workflow
        🚀 START
           │
           ▼
     Clone Repository
           │
           ▼
   Install Dependencies
           │
           ▼
 Add OpenRouter API Key
           │
           ▼
 Add Your .txt Documents
           │
           ▼
     python ingest.py
           │
           ▼
  streamlit run app.py
           │
           ▼
    Ask Questions
           │
           ▼
     🤖 AI Answer
     
🌟 Why RAG?
Traditional LLM
❓ Question
     ↓
   🤖 LLM
     ↓
✅ Answer
RAG
❓ Question
     ↓
🔎 Retrieve Knowledge
     ↓
📚 Relevant Documents
     ↓
🤖 LLM
     ↓
✅ Grounded Answer

RAG provides the LLM with relevant external information at query time instead of relying only on pretrained knowledge.

🔮 Future Improvements
<div align="center">
🔧 Improvement	Status
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
</div>
👨‍💻 Author
<div align="center">
Raj Yadav

B.Tech Computer Science Engineering

<br>

🤖 AI Engineering
🧠 Generative AI
🔎 RAG Systems
☁️ Cloud Computing
💻 Software Engineering

</div>
<div align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:8B5CF6,50:6366F1,100:00F7FF&height=120&section=footer&animation=fadeIn"/>
⭐ If you found this project useful, consider giving it a star!

Built with ❤️ using Python · LangChain · ChromaDB · Streamlit · OpenRouter

</div> ```
