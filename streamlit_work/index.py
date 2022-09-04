import streamlit as st
from PIL import Image

st.title('Streamlit app')

st.markdown('## Streamlit の紹介')
st.text('Python のフレームワーク, Streamlit の紹介です. このページは Streamlit を使って実装してます.')

# API Reference
st.markdown('---')
st.markdown('### API Reference')
link = '[Streamlit API](https://docs.streamlit.io/library/api-reference)'
comment = f'{link}: Streamlit の API については左こちらのリンクを参照してください.'
st.markdown(comment, unsafe_allow_html=True)

# st.code
st.markdown('---')
st.markdown('### code のサンプル')
link = '[code](https://docs.streamlit.io/library/api-reference/text/st.code)'
st.markdown(f'これは {link} を使ったサンプルです. ')

code = '''
import streamlit as st

st.title('Streamlit app')
'''
st.code(code, language='python')

# st.image
st.markdown('---')
st.markdown('### 画像貼付のサンプル')
link = '[image](https://docs.streamlit.io/library/api-reference/media/st.image)'
st.markdown(f'これは {link} を使ったサンプルです.')

image = Image.open('./assets/images/streamlit-logo-primary-colormark-darktext.png')
st.image(image)
logo = '[logo](https://streamlit.io/brand)'
st.markdown(f'( この {logo} は Streamlit の公式から拝借したものを使用しています.  )')


