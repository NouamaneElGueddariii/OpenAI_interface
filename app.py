import streamlit as st
import openai
import json 
import requests
from apikey import HuggingFace_key, openai_key
#openai.api_key =  st.secrets["opeanai_apikey"]

openai.api_key = openai_key
st.title("Liste von OpenAI-Modellen")

openai_models = openai.Model.list().data

frameworks =['Hugging Face','OpenAI']


framework_options = st.selectbox(
                        'Select a Framework:',
                         (frameworks)
)
if framework_options == "Hugging Face":
    #print(framework_options)
    ### hugging Face Part
    headers  = {"Authorization": f"Bearer {HuggingFace_key}"}
    list_models  = ["bert-base-uncased"]
    model_options = st.selectbox(
                        'Select a model:',
                        (list_models)
    )
    print(model_options)
    API_URL = f"https://api-inference.huggingface.co/models/{model_options}"
    st.write('options:',model_options)
    input = st.text_input("Enter your prompt here!")
    send = st.button('send request!')
    if send: 
        def query(payload):
            data = json.dumps(payload)
            response = requests.request("POST", API_URL, headers=headers, data = data)
            return json.loads(response.content.decode("utf-8"))
        
        data = query({"inputs": input})
        st.write(data)


if framework_options == "OpenAI":
    list_models  = []
    for model in openai_models: 
        list_models.append(model.id)

    print(framework_options)
    model_options = st.selectbox(
                        'Select a model:',
                        (list_models)
    )
    st.write('options:',model_options)
    temperature_option = st.selectbox(
                        'Select a temperature:',
                        (0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0)
    )
    st.write('Temperature:',temperature_option)
    #####

    input = st.text_input("Enter your prompt here!")
    send = st.button('send request!')
    if send: 
        response  = openai.ChatCompletion.create(
        model=model_options,
        temperature= temperature_option,
        messages=[
            {"role": "system", "content": "You are a helpful assistant.You shoudl answer the question to the best of your capabilities"},
            {"role": "user", "content": "you should answer the "},
            #{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": input}
        ]
        )
        st.write(response.choices[0].message.content)
# print(response)

# st.write(response)

