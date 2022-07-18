import imp
import streamlit as st
import numpy as np
from matplotlib import pyplot
from PIL import Image, ImageDraw, ImageFont
import os
import streamlit.components.v1 as components
from io import BytesIO
from SRGANupscaling.main import super_resolution_model
from SRGANupscaling.params import MODEL
import tensorflow_hub as hub

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the model (only executed once!)
@st.cache
def load_model():
	  return hub.load(MODEL)

model = load_model()

st.header("Pixel Perfect")
st.write("Upscale and enhance any image by using our SRGAN model.")
st.write("It can used for anything! From preserving old media material to \
         enhancing a microscope’s view, or identifying an individual in CCTV - \
         super-resolution’s impact is widespread and extremely evident.")

uploaded_file = st.file_uploader("Choose an image...")

if uploaded_file is not None:
    col1, col2 = st.columns([1,1])

    #src_image = load_image(uploaded_file)
    image = Image.open(uploaded_file)

    with col1:
        st.image(image, caption='Input Image', use_column_width=True)
    #st.write(os.listdir())

    with col2:
        im = super_resolution_model(image, model)
        st.image(im, caption='Output Image', use_column_width=True)

    # Convert Image?

    # if im.mode in ("RGBA", "P"):
    #     im = im.convert("RGB")

    rgb_im = im.convert('RGB')
    buf = BytesIO()
    rgb_im.save(buf, format="JPEG")
    byte_im = buf.getvalue()

    btn = st.download_button(
      label="Download Image",
      data=byte_im,
      file_name="imagename.png",
      mime="image/jpeg",
      )

with st.expander("How does it work?"):
     st.write("""
         To upscale your image, we use a SRGAN model to super-resolutionise your image with minimal information distortion.
     """)
