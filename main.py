import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="GOOGLE_API_KEY")

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
    
st.set_page_config(page_title='~Math Ninja~')
st.sidebar.header("Math Ninja")
st.sidebar.write("Using Google Gemini AI")
st.header("Math Ninja")
st.subheader("Upload a math problem image or enter a question to receive a step-by-step solution using Google's Gemini AI.")
input=st.text_input("What do you want me to do? ",key="input")
uploaded_file=st.file_uploader("choose an image",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

ssubmit=st.button("Generate Solutions")

input_prompt=
"""
You are an AI mathematics genius and tutor.
Your task is to solve mathematical problems accurately and clearly.

Guidelines:
- Explain the solution step by step.
- Show calculations wherever necessary.
- Keep the explanation concise but easy to understand.
- If the user only requests the final answer, provide it directly.
- If the uploaded image does not contain a math problem, politely inform the user.
"""

if ssubmit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know")
    st.write(response)
