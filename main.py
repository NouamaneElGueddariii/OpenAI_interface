import streamlit as st
import huggingface_api
import openai_api

st.title("Liste von OpenAI/HuggingFace-Modellen")
st.info("Hinweis: Für die Bert-Modelle muss das Wort [MASK] als Platzhalter verwendet werden, um Ergebnisse zu erhalten. Zum Beispiel: Hallo, ich bin ein [MASK]-Modell.")

framework_options = st.selectbox('Select a Framework:', ('Hugging Face', 'OpenAI'))

if framework_options == "Hugging Face":
    huggingface_api.run()
elif framework_options == "OpenAI":
    openai_api.run()