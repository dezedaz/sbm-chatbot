import streamlit as st
import openai
import os

# Charger les secrets Azure
openai.api_type = "azure"
openai.api_base = st.secrets["AZURE_OPENAI_ENDPOINT"]
openai.api_key = st.secrets["AZURE_OPENAI_API_KEY"]
openai.api_version = st.secrets["AZURE_OPENAI_API_VERSION"]
deployment_name = st.secrets["AZURE_OPENAI_DEPLOYMENT_NAME"]

# Interface
st.image("sbm_logo.png", width=150)
st.title("💻 SBM IT Chatbot")
st.markdown("Ask a question related to IT or your workstation. I will try to help you as your virtual assistant!")

# Interaction
question = st.text_input("💬 Your question:")

if question:
    try:
        response = openai.ChatCompletion.create(
            engine=deployment_name,
            messages=[
                {"role": "system", "content": "You are a helpful IT assistant for employees at SBM."},
                {"role": "user", "content": question}
            ],
            temperature=0.5,
            max_tokens=500
        )
        st.markdown(f"🧠 Response:\n\n{response['choices'][0]['message']['content']}")
    except Exception as e:
        st.error(f"❌ Azure API error: {e}")
