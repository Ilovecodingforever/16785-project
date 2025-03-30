import os

import torch
from transformers import pipeline

import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM


if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant",
         "content": "I am a human therapist. I want to be concise and empathetic. Don't list things. Be a good listener. "}]
if 'pipe_generate' not in st.session_state:
    st.session_state.pipe_generate = pipeline("text-generation", model="Qwen/Qwen2.5-7B-Instruct",
                                              device_map='auto', max_length=512)


text = st.text_input("text", )


if st.button("speak"):
    st.session_state.messages.append({"role": "user", "content": text})

    reply = st.session_state.pipe_generate(
        st.session_state.messages, max_length=1024)
    print(reply)
    reply = reply[-1]['generated_text'][-1]['content']
    st.session_state.messages.append({"role": "assistant", "content": reply})

    emotion = st.session_state.pipe_generate(
        [{"role": "user", "content":
            "classify this message and do not explain, is it happy, sad, surprise, fear, angry, or disgust: " + reply}],
        max_length=1024
    )[-1]['generated_text'][-1]['content']

    print(emotion)
    if 'happy' in emotion:
        emotion = 'happy'
    elif 'sad' in emotion:
        emotion = 'sad'
    elif 'surprise' in emotion:
        emotion = 'surprise'
    elif 'fear' in emotion:
        emotion = 'fear'
    elif 'angry' in emotion:
        emotion = 'angry'
    elif 'disgust' in emotion:
        emotion = 'disgust'
    else:
        emotion = 'default'

    # write to a file
    with open("script.txt", "w") as file:
        file.write(reply)
        file.write("\n")
        file.write(emotion)
        file.write("\n")
