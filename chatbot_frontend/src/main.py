import os
import requests
import streamlit as st

CHATBOT_URL = os.getenv(
    "CHATBOT_URL", "http://localhost:8000/hospital-rag-agent"
)

with st.sidebar:
    st.header("About")
    st.markdown(
        """
        This chatbot interfaces with a
        [LangChain](https://python.langchain.com/docs/get_started/introduction)
        agent designed to answer questions about UEFA Champions League.
        """
    )

    st.header("Example Questions")
    st.markdown("- Which teams are playing current champions league?")
    st.markdown(
        """- Which team scored the most goals on the opponent's pitch?"""
    )
    st.markdown(
        """- Which team scored the most goals on their own turf?"""
    )
    st.markdown(
        "- Which team has won the most games on its home turf?"
    )
    st.markdown(
        """- Which team has won the most games on its opponents' home turf"""
    )
    st.markdown(
        "- Which team has scored the most goals overall?"
    )
    st.markdown("- Which team has scored the fewest goals overall?")
    st.markdown(
        "- Which team has won the most matches?"
    )
    st.markdown("- Which team has lost the most games?")
    st.markdown(
        """- Which team has the highest average age?"""
    )
    st.markdown(
        "- Which team has the lowest average age?"
    )
    st.markdown(
        """- Who is the oldest player and which team does he play for?"""
    )
    st.markdown(
        """- Who is the youngest player and which team does he play for?"""
    )
    st.markdown(
        """- Which defender has scored the most goals?"""
    )
    st.markdown(
        """- Which player aged 20 or under has scored the most goals?"""
    )
    st.markdown("- Which player aged 30 or over has scored the most goals?")
    st.markdown(
        """- Which team scored the fewest goals on home turf?"""
    )


st.title("UEFA Champions League 2023-2024 Chatbot")
st.info(
    """Ask me questions about 2023-2024 UEFA Champions League!"""
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "output" in message.keys():
            st.markdown(message["output"])

        if "explanation" in message.keys():
            with st.status("How was this generated", state="complete"):
                st.info(message["explanation"])

if prompt := st.chat_input("What do you want to know?"):
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({"role": "user", "output": prompt})

    data = {"text": prompt}

    with st.spinner("Searching for an answer..."):
        response = requests.post(CHATBOT_URL, json=data)

        if response.status_code == 200:
            output_text = response.json()["output"]
            explanation = response.json()["intermediate_steps"]

        else:
            output_text = """An error occurred while processing your message.
            Please try again or rephrase your message."""
            explanation = output_text

    st.chat_message("assistant").markdown(output_text)
    st.status("How was this generated?", state="complete").info(explanation)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "output": output_text,
            "explanation": explanation,
        }
    )
