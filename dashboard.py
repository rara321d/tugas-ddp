import streamlit as st 

st.title("ini halaman dashboard!")
st.session_state['nabung']

jumlah = 0
for session in st.session_state['nabung']:
    jumlah = session['nominal']
    
st.write("total nominal menabung sebesar", jumlah)    
    