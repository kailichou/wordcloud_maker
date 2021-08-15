# ======== Import Libraries =========
from pickle import STOP
import streamlit as st
from langdetect import detect
from text_sample import paras
from wordcloud import WordCloud, STOPWORDS 
from config import FONT_PATH
import numpy as np
from PIL import Image
from io import BytesIO
import base64


# ========= Function =========
@st.cache
def make_cloud_array(txt, mask=None):
    wc = WordCloud(font_path=FONT_PATH+"roboto/Roboto-Regular.ttf", background_color="white", width=1600, height=800, stopwords=STOPWORDS, mask=mask).generate(txt)
    return wc.to_array()

def get_image_download_link(img):
	"""Generates a link allowing the PIL image to be downloaded
	in:  PIL image
	out: href string
	"""
	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/jpg;base64,{img_str}">Download result</a>'
	return href


# =========== Frontend =============
st.title("Make a WordCloud  Picture Today")
st.write("Let's start the party :smiley:.")
para = st.text_input("Please copy & paste your article/paragraph here...")
st.write("For example, Macbeth by Shakespeare :relaxed:")

if para:
    lang=detect(para)
    st.write("Nice, you wanna make a wordcloud picture in {}".format(lang))
    img_array = make_cloud_array(para, mask=None)
    st.image(img_array)
else:
    #st.write("Interesting, I can't recognise the language but let's make a wordcloud picture.")
    mask_example = np.array(Image.open("images/pngwing.com.png"))
    img_array = make_cloud_array(paras, mask=mask_example)
    st.image(img_array)

