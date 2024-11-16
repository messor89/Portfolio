import streamlit as st
from PIL import Image
import io
upload_iamge = st.file_uploader("Upload a filer")


if upload_iamge:
    img = Image.open(upload_iamge)
    grey_img = img.convert("L")
    st.image(grey_img)
    
    img_byte_arr = io.BytesIO()
    grey_img.save(img_byte_arr, format="PNG")
    img_byte_arr = img_byte_arr.getvalue()
    
    
    st.download_button(
        label="Download your picture",
        data=img_byte_arr,
        file_name="grayscale_image.png",
        mime="image/png"
    )