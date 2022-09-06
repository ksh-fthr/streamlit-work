import streamlit as st
import datetime

# st.form
st.markdown('### 入力ウィジェットを使った form のサンプル')
link_form = '[form](https://docs.streamlit.io/library/api-reference/control-flow)'
link_input_widjets = '[input widjets](https://docs.streamlit.io/library/api-reference/widgets#input-widgets)'
st.markdown(f'これは {link_input_widjets} を使った {link_form} のサンプルです. ')
st.markdown(f'入力ウィジェットについては {link_input_widjets} を参照してください.')

col1, col2 = st.columns(2)
with col1:
    st.caption('入力フォームのサンプル')
    with st.form(key='profile_form'):
        name = st.text_input('名前')
        address = st.text_input('住所')

        # select ボックスの場合は st.select とする
        age_category = st.radio('年齢層', ('18歳未満', '18歳以上'))

        hoby = st.multiselect(
            '趣味',
            ('スポーツ', '読書', 'プログラミング', '映画鑑賞', '釣り', '料理')
        )

        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')

        if submit_btn:
            st.text(f'ようこそ {name} さん. {address} に書籍を送りました.')
            st.text(f'年齢層: {age_category}')
            st.text(f'趣味: {", ".join(hoby)}')


with col2:
    st.caption('ウィジェットいろいろ')
    check_box = st.checkbox('チェックボックス')
    slider = st.slider('長さ', min_value=0, max_value=100)
    datepicker = st.date_input(
        '開始日',
        datetime.date(2022, 9, 1)
    )
    colorpicker = st.color_picker('テーマカラー', '#00f293')

