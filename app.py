import streamlit as st
from llm_api import generate_query

# --- Streamlit page setup ---
st.set_page_config(page_title="Needlu Chatbot", page_icon="🤖")
st.title("Needlu Chatbot")

st.write("Ask questions.")

# --- Initialize chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display previous messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- User input (chat mode) ---
if user_input := st.chat_input("Ask your question here..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                query = generate_query(user_input)
                st.markdown(f"**Generated Query / Expression:**\n```sql\n{query}\n```")
                st.session_state.messages.append({"role": "assistant", "content": f"```sql\n{query}\n```"})
            except Exception as e:
                error_msg = f"⚠️ Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

