import streamlit as st
import pandas as pd

# データ操作
st.markdown('### データ操作のサンプル')
df = pd.read_csv('./data/temperature.csv', index_col='月')

# レイアウト調整
col1, col2, col3 = st.columns(3)
with col1:
  st.caption('温度データをテーブルで表示')
  st.table(df)

with col2:
  st.caption('温度データを折れ線グラフで表示')
  st.line_chart(df)

with col3:
  st.caption('温度データを棒グラフで表示')
  st.bar_chart(df['2021年'])
  st.bar_chart(df['2022年'])

