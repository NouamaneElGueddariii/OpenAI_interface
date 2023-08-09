import json
import requests
import streamlit as st
from apikey import hugging_face_key
from huggingface_hub  import InferenceClient



def query(model_name, input_text):
    gen_kwargs = dict(
    max_new_tokens=512,
    top_k=30,
    top_p=0.9,
    temperature=0.2,
    repetition_penalty=1.02,
    stop_sequences=["\nUser:", "<|endoftext|>", "</s>"],
)
    if model_name == "Jukaboo/llama2-7b-jk-ft":
        endpoint_url =  "https://ceg49alq4qpkewtn.eu-west-1.aws.endpoints.huggingface.cloud"
        client = InferenceClient(endpoint_url , token=hugging_face_key) 
        response = client.text_generation(input_text, **gen_kwargs)
        return response

    else :
        headers = {"Authorization": f"Bearer {hugging_face_key}"}
        api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        payload = {"inputs": input_text}
        data = json.dumps(payload)
        response = requests.post(api_url, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))

def run():
    list_models = ["bert-base-uncased", "gpt2", "bert-base-multilingual-cased", "bert-large-cased","tiiuae/falcon-40b", "tiiuae/falcon-7b","Jukaboo/llama2-7b-jk-ft","meta-llama/Llama-2-7b-chat-hf"]
    model_options = st.selectbox('Select a model:', list_models)
    input_text = st.text_area("Enter your prompt here!")
    send = st.button('SEND REQUEST!')
    if send:
        data = query(model_options, input_text)
        st.write(data)






