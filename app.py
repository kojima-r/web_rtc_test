import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title('Streamlit App Test')
st.write('Hello world')

webrtc_streamer(key='example')
