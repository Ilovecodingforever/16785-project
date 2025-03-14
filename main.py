import os
os.environ['HF_HOME'] = '/home/scratch/mingzhul/.cache/huggingface'

import torch
from transformers import pipeline

import streamlit as st





def generate_text(messages):
    pipe = pipeline("text-generation", model="Qwen/Qwen2.5-7B-Instruct", device='cpu')
    print(messages)
    print(pipe(messages))
    return pipe(messages)[0]['generated_text'][1]['content']



if 'messages' not in st.session_state:
    st.session_state.messages = []

text = st.text_input("text", )


if st.button("speak"):
    st.session_state.messages.append({"role": "user", "content": text})

    reply = generate_text(st.session_state.messages)
    st.session_state.messages.append({"role": "robot", "content": reply})

    # write to a file
    with open("script.txt", "w") as file:
        file.write(reply)
    
