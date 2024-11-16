import streamlit as st
from PIL import Image

upload_iamge = st.file_uploader("Upload a filer")


if upload_iamge:
    img = Image.open(upload_iamge)
    grey_img = img.convert("L")
    st.image(grey_img)

