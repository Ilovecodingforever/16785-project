import streamlit as st
# from pylips.speech import RobotFace
# from script_reading import read

def speak(text):
    face.say(text)


# @st.cache_resource
def init():
    face = RobotFace()
    return face


# import os
# os.system('dir c:\\')

# face = init()
text = st.text_input("text", )
if st.button("speak"):
    # exec(open("pylips_face_start.py").read())
    
    # script = '''FARQUAAD: I've tried to be fair to you. Now my patience has reached its end. Tell me or I'll...'''
    # read(script)
    
    # write to a file
    with open("script.txt", "w") as file:
        file.write(text)
    
    # exec(open("script_reading.py").read())
    
    # face = init()
    # speak(text)
