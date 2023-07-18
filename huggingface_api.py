import json
import requests
import streamlit as st

hugging_face_key = st.secrets["hugging_face_key"]
#hugging_face_key = HuggingFace_key



def query(model_name, input_text):
    headers = {"Authorization": f"Bearer {hugging_face_key}"}
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    payload = {"inputs": input_text}
    data = json.dumps(payload)
    response = requests.post(api_url, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

def run():
    list_models = ["bert-base-uncased", "gpt2", "bert-base-multilingual-cased", "bert-large-cased","tiiuae/falcon-40b", "tiiuae/falcon-7b"]
    model_options = st.selectbox('Select a model:', list_models)
    input_text = st.text_area("Enter your prompt here!")
    send = st.button('SEND REQUEST!')
    if send:
        data = query(model_options, input_text)
        st.write(data)






