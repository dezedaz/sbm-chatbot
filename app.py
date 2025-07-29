import streamlit as st
import requests
from PIL import Image

# Page setup
st.set_page_config(
    page_title="SBM IT Chatbot",
    page_icon="💻",
    layout="centered",
    initial_sidebar_state="auto"
)

# Display logo
logo = Image.open(".streamlit/sbm_logo.png")
st.image(logo, width=180)

# App title
st.title("💻 SBM IT Chatbot")
st.write("Ask a question related to IT or your workstation. I will try to help you as your virtual assistant!")

# Load secrets
API_KEY = st.secrets["AZURE_FOUNDY_API_KEY"]
ENDPOINT = st.secrets["AZURE_FOUNDY_ENDPOINT"]

# Headers for the Azure Foundry API
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# User input
question = st.text_input("💬 Your question:")

if question:
    with st.spinner("Thinking..."):
        # Format message for Azure AI
        payload = {
            "messages": [
                {"role": "system", "content": "You are an assistant helping employees at Saudi Business Machines (SBM) with IT-related issues."},
                {"role": "user", "content": question}
            ]
        }

        try:
            response = requests.post(
                ENDPOINT,
                headers=headers,
                json=payload
            )
            data = response.json()

            if "choices" in data and data["choices"]:
                answer = data["choices"][0]["message"]["content"]
                st.success(answer)
            else:
                st.error("No response received from Azure Foundry.")

        except Exception as e:
            st.error(f"Connection error with Azure Foundry: {e}")

