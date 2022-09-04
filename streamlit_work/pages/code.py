import streamlit as st

# st.code
st.markdown('### code のサンプル')
link = '[code](https://docs.streamlit.io/library/api-reference/text/st.code)'
st.markdown(f'これは {link} を使ったサンプルです. ')

code = '''
import streamlit as st

st.title('Streamlit app')
'''
st.code(code, language='python')

