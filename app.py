import streamlit as st
import requests

st.set_page_config(page_title="SBM IT Chatbot", page_icon="💬", layout="centered")

# ✅ Logo SBM (placé dans .streamlit/sbm_logo.png)
st.image(".streamlit/sbm_logo.png", width=150)

# ✅ Titre et description
st.title("💻 SBM IT Chatbot")
st.write("Ask a question related to IT or your workstation. I will try to help you as your virtual assistant!")

# ✅ Lecture des secrets (clé + endpoint Azure Foundry)
API_KEY = st.secrets["AZURE_FOUNDY_API_KEY"]
ENDPOINT = st.secrets["AZURE_FOUNDY_ENDPOINT"]

# ✅ Saisie utilisateur
question = st.text_input("💬 Your question:")

if question:
    # ✅ Préparation de la requête
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [
            {"role": "system", "content": "You are an IT support assistant for SBM employees."},
            {"role": "user", "content": question}
        ]
    }

    # ✅ Appel Azure Foundry
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        data = response.json()

        if "choices" in data:
            reply = data["choices"][0]["message"]["content"]
            st.success(reply)
        else:
            st.error("⚠️ Azure response missing 'choices' — check API format or endpoint.")

    except Exception as e:
        st.error(f"❌ Azure Foundry error: {e}")




