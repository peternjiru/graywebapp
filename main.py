import streamlit as st
from PIL import Image # PIL installed when streamlit is installed

st.subheader("Color to Grayscale convertor")

# upload image and save to variable
uploaded_image = st.file_uploader("Upload Image")

if uploaded_image:
    # create pillow image instance
    img = Image.open(uploaded_image)
    # convert image to grayscale
    gray_image = img.convert("L")
    # render grayscale image on the web page
    st.image(gray_image)

with st.expander("Start Camera"):
    #start camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # create pillow image instance
    img = Image.open(camera_image)
    # convert image to grayscale
    gray_image = img.convert("L")
    # render grayscale image on the web page
    st.image(gray_image)