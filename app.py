import streamlit as st 

# st.write('hello world!')
if "nabung" not in st.session_state:
    st.session_state['nabung'] = []

dashboard = st.Page("./pages/dashboard.py", title="Dashboard")
nabung = st.Page("./pages/nabung.py", title="nabung")

pg = st.navigation({
    "Dashboard" : [dashboard],
    "Nabung" : [nabung],
})

    
pg.run()