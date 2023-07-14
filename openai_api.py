import openai
import streamlit as st
import re 
import tiktoken


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
    """ Return the number of tokens """
    try: 
         encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif  model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4
        tokens_per_name = -1 
    elif "gpt-3.5-turbo" in model:
        print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
        return token_counter(prompt, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
        return token_counter(prompt, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""token_counter() is not implemented for model {model}."""
        )
    num_tokens = 0
    for message in prompt:
        num_tokens += tokens_per_message
        print(message)
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens

## neue Feature für die compliance(moderieren von Nachrichten)
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
        col1, col2, col3, col4, col5= st.columns(5)

        send = col1.button('SEND REQUEST!')
        counter = col5.button('COUNT TOKENS!')
        if counter:
                print(model_options)
                print(input)
                num_tokens = token_counter(model_options, input)
                st.write("Number of tokens:", num_tokens)
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
        col1, col2, col3, col4, col5= st.columns(5)

        send = col1.button('SEND REQUEST!')
        counter = col5.button('COUNT TOKENS!')
        messages=[
                    {"role": "system", "content": "You are a helpful assistant.You should answer the question to the best of your capabilities"},
                    {"role": "user", "content": input}
                ]
        if counter:
            num_tokens =  token_counter(model_options, messages)
            st.write("Number of tokens:", num_tokens)
      
        if send: 
            response  = openai.ChatCompletion.create(
            model=model_options,
            temperature= temperature_option,
            messages=messages
                )
            st.write(response.choices[0].message.content)   
