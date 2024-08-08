import streamlit as st
st.header('Restrunt App')
dic = {'Tea': 20, 'Coffee': 40, 'Cold Coffee': 50, 'Cold Drink': 45, 'Snacks': 60}
dict = {}
menu = st.radio('Show Menu', options=['No','Yes'])
if menu == 'Yes':
    for i in dic:
        st.checkbox(i)
        