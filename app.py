import streamlit as st

st.set_page_config(page_title="SBM Chatbot", page_icon="🧠")

st.title("SBM IT Chatbot 💬")
st.write("Posez-moi une question technique liée à votre poste de travail ou votre environnement IT.")

# Placeholder for future chatbot logic
question = st.text_input("💻 Votre question :", "")
if question:
    st.info("💡 (Réponse IA ici bientôt...)")
