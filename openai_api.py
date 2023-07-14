import openai
import streamlit as st
import re 
import tiktoken
from apikey import openai_key


openai.api_key = st.secrets["openai_apikey"]
#openai.api_key = openai_key

def query(model_name, temperature, input_text):
    response = openai.ChatCompletion.create(
        model=model_name,
        temperature=temperature,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You should answer the question to the best of your capabilities."},
            {"role": "user", "content": input_text}
        ]
    )
    return response.choices[0].message.content

def token_counter(model, prompt):
    pass
def moderations():
    pass


def run():
    openai_models = openai.Model.list().data
    list_models = [model.id for model in openai_models]
    model_options = st.selectbox('Select a model:', list_models)
    if re.search(r'text-(babbage|davinci|curie|ada)',model_options): 

        st.write('Temperature:',model_options)
        temperature_option = st.selectbox(
                            'Select a temperature:',
                            (0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0)
        )
        st.write('Temperature:',temperature_option)

        input = st.text_area("Enter your prompt here!")
        send = st.button('SEND REQUEST!')
        #token_counter = st.button('count tokens')

        if send: 
                response = openai.Completion.create(
                                model=model_options,
                                prompt= input
                                )
                st.write(response.choices[0]) 

    if re.search(r'\b(gpt)\b',model_options): 
        st.write('Temperature:',model_options)
        temperature_option = st.selectbox(
                            'Select a temperature:',
                            (0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0)
        )
        st.write('Temperature:',temperature_option)
        #####

        input = st.text_area("Enter your prompt here!")
        send = st.button('SEND REQUEST!')
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
