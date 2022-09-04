import streamlit as st
from PIL import Image

# st.image
st.markdown('### 画像貼付のサンプル')
link = '[image](https://docs.streamlit.io/library/api-reference/media/st.image)'
st.markdown(f'これは {link} を使ったサンプルです.')

# 画像への path は プロジェクトのルートディレクトリからの相対 path で指定する
image = Image.open('./assets/images/streamlit-logo-primary-colormark-darktext.png')
st.image(image)

logo = '[logo](https://streamlit.io/brand)'
st.markdown(f'( この {logo} は Streamlit の公式から拝借したものを使用しています.  )')


