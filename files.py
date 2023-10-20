import streamlit as st
import pandas as pd

st.subheader('Uploading the csv Files')
csv_file = st.file_uploader("Upload csv File : ", type =['csv', 'xlsx'])

st.subheader('Loading the csv Files')
df = pd.read_csv('Products.csv')
if df is not None:
    st.table(df.head())

st.subheader('Working  with Image Files')
img_file = st.file_uploader("Upload Image File : ", type = ['png', 'jpeg'])
if img_file is not None:
    st.image(img_file)

st.subheader('Working  with Video Files')
video_file = st.file_uploader("Upload Video File : ", type = ['mkv','mp4'])
if video_file is not None:
    st.video(video_file)

st.subheader('Working  with Audio Files')
audio_file = st.file_uploader("Upload Audio File : ", type = ['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file.read())
