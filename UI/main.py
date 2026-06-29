import streamlit as st
from pages import *

st.set_page_config(
    page_title="Wati Statistics",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("Navigation")
st.title("📊 Wati Statistics")

st.markdown("""
    Welcome to the **Wati Statistics Dashboard**

    Use the sidebar to view:

    - 👨‍🎓 Student Details
    - 💬 Conversation Details
    - 👨‍💼 Operator Details
    - 📌 Event Details
    """)

col1, col2 = st.columns(2)

with col1:
    st.info("View student records")

with col2:
    st.success("Track WATI statistics")
    
page = st.sidebar.radio(
    "Select Page",
    [
        "👨‍🎓 Student Details",
        "💬 Conversation Details",
        "👨‍💼 Operator Details",
        "📌 Event Details"
    ]
)

if page == "👨‍🎓 Student Details":
    studentDetails_UI()
elif page == "💬 Conversation Details":
    conversationDetails_UI()
elif page == "👨‍💼 Operator Details":
    operatorDetails_UI()
elif page == "📌 Event Details":
    eventDetails_UI()