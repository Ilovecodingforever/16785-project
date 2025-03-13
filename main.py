import streamlit as st
# from pylips.speech import RobotFace
# from script_reading import read
import os
os.environ['HF_HOME'] = '/home/scratch/mingzhul/.cache/huggingface'

# from pylips.speech import RobotFace
# from pylips.face import FacePresets

import torch
from transformers import pipeline




# def speak(text):
#     face.say(text)


# # @st.cache_resource
# def init():
#     face = RobotFace()
#     return face


# @st.cache_resource
# def generate_text(messages="Who are you?"):
#     messages = [
#         {"role": "user", "content": messages},
#     ]
#     # pipe = pipeline("text-generation", model="NousResearch/Hermes-3-Llama-3.2-3B")
#     # pipe = pipeline("text-generation", model="SweatyCrayfish/llama-3-8b-quantized", device_map='auto')
#     # model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
#     # pipe = pipeline(
#     #     "text-generation",
#     #     model=model_id,
#     #     model_kwargs={"torch_dtype": torch.bfloat16},
#     #     device_map="auto",
#     # )
#     # pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3", device_map='auto')
#     # pipe = pipeline("text-generation", model="MaziyarPanahi/Mistral-7B-Instruct-v0.3-GGUF")
#     pipe = pipeline("text-generation", model="Qwen/Qwen2.5-7B-Instruct", device_map='auto')
#     print(messages)
#     print(pipe(messages))

#     return pipe(messages)[0]['generated_text'][1]['content']





def generate_text(messages="Who are you?"):
    messages = [
        {"role": "user", "content": messages},
    ]

    pipe = pipeline("text-generation", model="Qwen/Qwen2.5-7B-Instruct", device_map='auto')
    print(messages)
    print(pipe(messages))

    return pipe(messages)[0]['generated_text'][1]['content']



# import os
# os.system('dir c:\\')

# face = init()
text = st.text_input("text", )
if st.button("speak"):
    # exec(open("pylips_face_start.py").read())
    
    # script = '''FARQUAAD: I've tried to be fair to you. Now my patience has reached its end. Tell me or I'll...'''
    # read(script)
    reply = generate_text(text)

    # write to a file
    with open("script.txt", "w") as file:
        file.write(reply)
    
    # exec(open("script_reading.py").read())
    
    # face = init()
    # speak(text)
