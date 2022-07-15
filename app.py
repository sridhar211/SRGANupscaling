import streamlit as st
import numpy as np
from matplotlib import pyplot
from PIL import Image, ImageDraw, ImageFont
import os
import streamlit.components.v1 as components
from io import BytesIO
from SRGANupscaling.main import super_resolution
import time

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.set_page_config(
    page_title="Pixel Perfect",
    page_icon="💫",
    layout="centered",
    initial_sidebar_state="auto",
)

# st.header("Pixel Perfect")
main_image = Image.open('static/main_banner.png')
st.image(main_image,use_column_width='auto')
st.title("Upscale and enhance any image by using our SRGAN model.")
st.write("It can used for anything! From preserving old media material to \
         enhancing a microscope’s view, or identifying an individual in CCTV - \
         super-resolution’s impact is widespread and extremely evident.")



st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.info("✨ It can used for anything! From preserving old media material to \
         enhancing a microscope’s view, or identifying an individual in CCTV - \
         super-resolution’s impact is widespread and extremely evident.😉")

uploaded_file = st.file_uploader("Upload Image 🚀", type=["png","jpg","bmp","jpeg"])





if uploaded_file is not None:
    col1, col2 = st.columns([1,1])

    #src_image = load_image(uploaded_file)
    image = Image.open(uploaded_file)

    with col1:
        st.markdown("---")
        st.image(image, caption='Input Image', use_column_width=True)

    #st.write(os.listdir())

    with col2:
        im = super_resolution(image)
        st.markdown("---")
        st.image(im,  caption='Output Image', use_column_width=True)



    # Convert Image?

    # if im.mode in ("RGBA", "P"):
    #     im = im.convert("RGB")

    rgb_im = im.convert('RGB')
    buf = BytesIO()
    rgb_im.save(buf, format="JPEG")
    byte_im = buf.getvalue()

    if st.download_button(
      label="Download Image ",
      data=byte_im,
      file_name=str("super " + uploaded_file.name),
      mime="image/jpeg",

      ):

        st.balloons()
        st.success('✅ Download Successful !!')




else:
    st.warning('⚠ Please upload your Image file 😯')

# import time

# my_bar = st.progress(0)

# for percent_complete in range(100):
#      time.sleep(0.1)
#      my_bar.progress(percent_complete + 1)


with st.expander("How does it work?"):
     st.write("""
         To upscale your image, we use a SRGAN model to super-resolutionise your image with minimal information distortion.
     """)
st.markdown("<br><hr><center>Enjoy ❤️</center><hr>", unsafe_allow_html=True)
