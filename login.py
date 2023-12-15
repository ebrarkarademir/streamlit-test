import streamlit as st

def run():
    st.title("Login")
    username = st.text_input("Username", placeholder="admin")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "1" and password == "1":
            st.session_state['loggedin'] = True
        else:
            st.error("Incorrect username or password")
        
if __name__ == "__main__":
    run()
    
