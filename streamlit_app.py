from datetime import datetime
import streamlit as st

# Title of the app
st.title('Bitcoin Timestamp AI Converter')

# Input section
st.subheader('Convert Bitcoin Transaction Timestamp to Human-Readable Date')
timestamp = st.number_input('Enter a Unix Timestamp:', value=1734141600)

# Convert timestamp
try:
    human_readable_date = datetime.utcfromtimestamp(timestamp)
    st.write(f"**Date:** {human_readable_date}")
except ValueError:
    st.error("Invalid timestamp. Please enter a valid Unix timestamp.")

# Footer
st.write("---")
st.caption("Developed by Abdulhakim Ahmad")
