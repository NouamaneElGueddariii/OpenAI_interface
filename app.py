import streamlit as st
import openai


OPENAI_API_KEY ="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"
openai.api_key =  OPENAI_API_KEY


st.title("Liste von OpenAI-Modellen")

openai_models = openai.Model.list().data
list_models  = []

for model in openai_models: 
    list_models.append(model.id)
    

##### Options
model_option = st.selectbox(
                     'Select a model:',
                     (list_models)
)
st.write('options:',model_option)
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
    model=model_option,
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