import os
import streamlit as st

from rag import stream_answer, get_sources


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI RAG Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: #0e1117;
    }

    /* Header */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #9ca3af;
        font-size: 17px;
        margin-bottom: 30px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #151922;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        border-radius: 14px;
        padding: 12px 16px;
        margin-bottom: 10px;
    }

    /* Chat input */
    [data-testid="stChatInput"] {
        border-radius: 14px;
    }

    /* Source box */
    .source-box {
        background: #171b24;
        border-radius: 10px;
        padding: 12px;
        margin-top: 10px;
        color: #cbd5e1;
        font-size: 14px;
    }

    /* Status card */
    .info-card {
        background: #171b24;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🤖 AI RAG Chatbot")

    st.markdown("---")

    st.markdown(
        """
        ### About

        This chatbot uses:

        - 📚 Document retrieval
        - 🧠 Embeddings
        - 🗄️ Chroma vector database
        - 💬 Conversation memory
        - ⚡ Streaming responses
        - 🌐 OpenRouter
        """
    )

    st.markdown("---")

    st.markdown("### ⚙️ Settings")

    show_sources = st.checkbox(
        "Show sources",
        value=True
    )

    st.markdown("---")

    if st.button(
        "🗑️ Clear conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.markdown("---")

    st.caption(
        "Powered by Streamlit + LangChain + Chroma + OpenRouter"
    )


# ============================================================
# INITIALIZE CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🤖 AI RAG Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Ask questions about your documents using Retrieval-Augmented Generation
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# WELCOME MESSAGE
# ============================================================

if len(st.session_state.messages) == 0:

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        st.markdown(
            """
            👋 **Hey! I'm your RAG chatbot.**

            Ask me anything about the documents you loaded.

            For example:

            - Tell me about Google
            - What products does Microsoft offer?
            - What does NVIDIA do?
            - Compare Google and Microsoft
            """
        )


# ============================================================
# DISPLAY PREVIOUS MESSAGES
# ============================================================

for message in st.session_state.messages:

    avatar = (
        "👤"
        if message["role"] == "user"
        else "🤖"
    )

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):

        st.markdown(
            message["content"]
        )

        # Show sources if available
        if (
            message["role"] == "assistant"
            and show_sources
            and message.get("sources")
        ):

            with st.expander("📚 Sources"):

                for source in message["sources"]:

                    st.write(
                        f"• {source}"
                    )


# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "Ask something about your documents..."
)


# ============================================================
# HANDLE NEW QUESTION
# ============================================================

if question:

    # --------------------------------------------------------
    # SHOW USER MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(question)


    # --------------------------------------------------------
    # AI RESPONSE
    # --------------------------------------------------------

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        response_placeholder = st.empty()

        try:

            # Get history BEFORE adding current assistant answer
            history = st.session_state.messages[:-1]

            # Stream response
            answer = st.write_stream(
                stream_answer(
                    question,
                    history
                )
            )

            # Make sure answer is a string
            if not isinstance(answer, str):

                answer = str(answer)


            # ------------------------------------------------
            # GET SOURCES
            # ------------------------------------------------

            sources = []

            if show_sources:

                sources = get_sources(question)


                if sources:

                    with st.expander("📚 Sources"):

                        for source in sources:

                            st.write(
                                f"• {source}"
                            )


            # ------------------------------------------------
            # SAVE ASSISTANT MESSAGE
            # ------------------------------------------------

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                }
            )


        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )