import streamlit as st
import requests

st.set_page_config(page_title="SBM Chatbot", page_icon="💬")

st.title("🤖 SBM IT Chatbot")
st.write("Pose une question liée à l'informatique ou à ton poste de travail.")

API_KEY = st.secrets["AZURE_FOUNDY_API_KEY"]
ENDPOINT = st.secrets["AZURE_FOUNDY_ENDPOINT"]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

question = st.text_input("💬 Votre question :")

if question:
    payload = {
        "messages": [
            {"role": "system", "content": "Tu es un assistant pour les employés IT de SBM."},
            {"role": "user", "content": question}
        ]
    }

    try:
        response = requests.post(
            f"{ENDPOINT}/chat/completions",
            headers=headers,
            json=payload
        )
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        st.success(reply)
    except Exception as e:
        st.error(f"Erreur de connexion à Azure Foundry : {e}")
