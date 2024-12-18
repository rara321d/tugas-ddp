import streamlit as st 

st.title("ini halaman nabung!")

with st.form("nabung"): 
    nama = st.text_input("masukkan nama")
    nominal = st.number_input("masukkan nominal nabung")
    submitButton = st.form_submit_button("simpan")
    
    if submitButton:
        st.write(nama)
        st.session_state["nabung"].append({
            "nama" : nama,
            "nominal" : nominal,
        })
        st.success("berhasil menabung!")