import streamlit as st
import pandas as pd

# データ操作
st.markdown('### データ操作のサンプル')

df = pd.read_csv('./data/temperature.csv', index_col='月')
st.caption('温度データをテーブルで表示')
st.table(df)

st.caption('温度データをグラフで表示')
st.line_chart(df)
st.bar_chart(df['2021年'])
st.bar_chart(df['2022年'])
