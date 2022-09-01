import streamlit as st

st.title('Streamlit app')

st.markdown('## Streamlit の紹介')
st.text('Python のフレームワーク, Streamlit の紹介です. このページは Streamlit を使って実装してます.')


st.markdown('---')
st.markdown('### API Reference')
link = '[Streamlit API](https://docs.streamlit.io/library/api-reference)'
comment = f'{link}: Streamlit の API については左こちらのリンクを参照してください.'
st.markdown(comment, unsafe_allow_html=True)


st.markdown('---')
st.markdown('### code のサンプル')
link = '[code](https://docs.streamlit.io/library/api-reference/text/st.code)'
st.markdown(f'これは {link} を使ったサンプルです. ')

code = '''
import streamlit as st

st.title('Streamlit app')
'''
st.code(code, language='python')

