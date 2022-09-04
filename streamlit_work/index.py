import streamlit as st
from PIL import Image

st.title('Streamlit app')

st.markdown('## Streamlit の紹介')
st.text('Python のフレームワーク, Streamlit の紹介です. このページは Streamlit を使って実装してます.')

# API Reference
st.markdown('### API Reference')
link = '[Streamlit API](https://docs.streamlit.io/library/api-reference)'
comment = f'{link}: Streamlit の API については左こちらのリンクを参照してください.'
st.markdown(comment, unsafe_allow_html=True)

