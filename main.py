import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Streamlit 入門')


df = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
if st.checkbox('地図'):
    st.map(df)

option = st.selectbox(
    "好きな数字を教えてください。",
    list(range(1, 11))
)

if st.checkbox('占い結果'):
    option, 'を選んだあなたは天才ではないです'

text = st.text_input('趣味を教えてください')
'あなたの趣味：', text

condition = st.slider('あなたのコンディションは？', 0, 100, 50)
'あなたのコンディション：', condition

st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

left_column, right_column = st.columns(2)
button = left_column.button('左カラムを表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('志望校を教えてください')
expander.write('東大')

'start!!!'
latest_text = st.empty()
bar = st.progress(0)


for i in range(1,101):
    latest_text.text(f'latest {i}')
    bar.progress(i)
    time.sleep(0.01)

'done!!!'
# このスリープは毎回実行されるから重くなる。画面の下におけばまあいいかも。
