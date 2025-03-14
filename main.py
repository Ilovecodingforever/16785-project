import os
os.environ['HF_HOME'] = '/home/scratch/mingzhul/.cache/huggingface'

import torch
from transformers import pipeline

import streamlit as st




if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'pipe' not in st.session_state:
    st.session_state.pipe = pipeline("text-generation", model="Qwen/Qwen2.5-7B-Instruct", device_map='auto')





text = st.text_input("text", )


if st.button("speak"):
    st.session_state.messages.append({"role": "user", "content": text})

    reply = st.session_state.pipe(st.session_state.messages)[0]['generated_text'][1]['content']
    st.session_state.messages.append({"role": "robot", "content": reply})

    # write to a file
    with open("script.txt", "w") as file:
        file.write(reply)

