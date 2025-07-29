import streamlit as st
import requests

st.set_page_config(page_title="SBM IT Chatbot", page_icon="💻")
st.image("sbm_logo.png", width=150)  # Assure-toi d’avoir ce fichier dans le repo

st.title("💻 SBM IT Chatbot")
st.write("Ask a question related to IT or your workstation. I will try to help you!")

# Récupération des clés depuis secrets.toml
API_KEY = st.secrets["AZURE_FOUNDY_API_KEY"]
ENDPOINT = st.secrets["AZURE_FOUNDY_ENDPOINT"]
DEPLOYMENT_NAME = "gpt-35-turbo"  # Remplace par le nom exact de ton déploiement

# Configuration de la requête
url = f"{ENDPOINT}/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version=2024-02-15-preview"
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY
}

# Saisie utilisateur
question = st.text_input("💬 Your question:")

if question:
    with st.spinner("Thinking..."):
        payload = {
            "messages": [
                {"role": "system", "content": "You are an IT assistant for SBM employees."},
                {"role": "user", "content": question}
            ]
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            try:
                st.success(result["choices"][0]["message"]["content"])
            except Exception as e:
                st.error("The response format is unexpected.")
        else:
            st.error(f"Azure Error {response.status_code}: {response.text}")



