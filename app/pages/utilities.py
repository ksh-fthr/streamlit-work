import streamlit as st

st.markdown('### Utilities のサンプル')
utilities_link = '[Utilities](https://docs.streamlit.io/library/api-reference/utilities)'
st.markdown(f'ここでは {utilities_link} を扱ったサンプルを実装します. ')

# タブ利用時は複数用意する
# リストの中身が一つだけだと with で object を指定した際に実行時エラーとして下記が発生する
#
# ```:エラー
# ValueError: not enough values to unpack (expected 2, got 1)
# ```
tab_page_config, tab_echo = st.tabs(["set_page_config", "echo"])


with tab_page_config:
    st.markdown('#### st.set_page_conofig のサンプル')
    st_set_page_config_link = '[st.set_page_config](https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config)'
    st.markdown(f'以下は {st_set_page_config_link} のサンプルコードです')

    code = '''
    st.set_page_config(
      page_title="Ex-stream-ly Cool App",
      page_icon="🧊",
      layout="wide",
      initial_sidebar_state="expanded",
      menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
      }
    )
    '''
    st.code(code, language='python')

    st.write('reference には下記注釈が記載されています')
    note = '''
      This must be the first Streamlit command used in your app, and must only be set once.
    '''
    st.code(note)
    st.write('set_page_config を利用する場合は上記注釈にご留意ください')

with tab_echo:
    st.markdown('#### st.echo のサンプル')
    st_echo_link = '[st.echo](https://docs.streamlit.io/library/api-reference/utilities/st.echo)'
    st.markdown(f'以下は {st_echo_link} のサンプルです')

    with st.echo():
        # `st.echo` の中に記載された内容は `code` ブロックとして扱われ描画されます.
        # ただし, ブロック内に定義されたメソッドや実行文は処理されます.
    
        # ユーザ名取得
        def get_user_name():
            return 'John'
    
        # 句読点取得
        def get_punctuation():
            return '!!!'
    
        greeting = "Hi there, "
        value = get_user_name()          # code ブロックに描画されるとともに実行もされている
        punctuation = get_punctuation()  # ここも同じ
    
        # ここも code ブロックに描画されるとともに実行される
        # この write 文はコードブロックの外側で出力される
        st.write(greeting, value, punctuation) # Hi there, John !!!
    
    # `st.code` ブロックから外れたので通常どおりに実行される
    st.write('Done!')

