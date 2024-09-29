import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyA_FNmEtuE4DD70o1QrzYnI3QWidJrptWo")

model=genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text,image_data,prompt):
    response=model.generate_content([input_text,image_data[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded")
    
st.set_page_config(page_title='~ Invoice ~')
st.sidebar.header("Math Ninja")
st.sidebar.write("Courtesy of Avo")
st.sidebar.write("Using google gemini AI")
st.header("Math Ninja")
st.subheader("Courtesy of Avo")
st.subheader("Get all your math answers!!!")
input=st.text_input("What do you want me to do? ",key="input")
uploaded_file=st.file_uploader("choose an image",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

ssubmit=st.button("Continuee")

input_prompt="""
you are a math genuis. you can take any math questions from the user and solve it according to their needs
be polite and use unifrom text. give them steps when asked. 
"""

if ssubmit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know")
    st.write(response)
