import streamlit as st
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express




def run():
    
    # Sidebar content
    with st.sidebar:
        st.header('Admin Panel')
        st.button('Tab1')
        st.button('Tab2')
        # Add more buttons or links as seen in the screenshot

    # Main content
    with st.container():
        st.title('Tab1')

        # Asset Status Section
        with st.expander("Asset Status: Clustered_Cycle", expanded=True):
            st.error('OFF 1')  # Change as required

        # Telemetry Cards Section
        with st.expander("Telemetry Cards", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="telemetry", value="0s")

        # Test Asset id Section
        with st.expander("Test_Asset_id", expanded=True):
            st.text('Test_Asset_id : [TO] Test_Asset_id')
            # You can add more interactive widgets here as needed
    st.markdown(
        """
        <style>
        /* This targets the sidebar background */
        .css-1e5imcs {
            width: 50px !important; /* Adjust the width as needed and use !important to override existing styles */
        }
        /* You might need to target other classes or attributes depending on the structure */
        </style>
        """,
        unsafe_allow_html=True
    )
    # Add footer or additional content as needed
if __name__ == "__main__":
    run()
    