import os
os.environ['HF_HOME'] = '/home/scratch/mingzhul/.cache/huggingface'

import torch
from transformers import pipeline

import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM




if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'pipe_generate' not in st.session_state:
    # st.session_state.model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-7B-Instruct")
    # st.session_state.pipe_generate = pipeline("text-generation", st.session_state.model, 
    st.session_state.pipe_generate = pipeline("text-generation", model="Qwen/Qwen2.5-7B-Instruct", 
                                              device_map='auto', max_length=512)
    # st.session_state.pipe_classify = pipeline("text-classification", model="Qwen/Qwen2.5-7B-Instruct", 
    #                                           device_map='auto', max_length=512)




text = st.text_input("text", )


if st.button("speak"):
    st.session_state.messages.append({"role": "user", "content": text})

    # tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")
    # pipe = pipeline("text-generation", st.session_state.model, tokenizer=tokenizer,
                    # device_map='auto', max_length=512)
    reply = st.session_state.pipe_generate(st.session_state.messages)
    # reply = pipe(st.session_state.messages)
    print(reply)
    reply = reply[-1]['generated_text'][-1]['content']
    st.session_state.messages.append({"role": "robot", "content": reply})
    
    # st.session_state.model.to('cpu')
    
    emotion = st.session_state.pipe_generate(
        [{"role": "user", "content": 
            "classify this message and do not explain, is it happy, sad, surprise, fear, angry, or disgust: " + reply}]
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

