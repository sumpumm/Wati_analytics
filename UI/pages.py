import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def studentDetails_UI():
    st.title("STUDENT DATA")

    try:
        df = pd.read_csv(
            BASE_DIR/'data/studentDetails.csv',
            delimiter="|",
            encoding="utf-8"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.write(f"Total Students: {len(df)}")

    except FileNotFoundError:
        st.error("CSV file not found.")
    except Exception as e:
        st.error(f"Error: {e}")

def operatorDetails_UI():
    st.title("Operator DATA")

    try:
        df = pd.read_csv(
            BASE_DIR/'data/operatorDetails.csv',
            delimiter="|",
            encoding="utf-8"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.write(f"Total Students: {len(df)}")

    except FileNotFoundError:
        st.error("CSV file not found.")
    except Exception as e:
        st.error(f"Error: {e}")
        
def conversationDetails_UI():
    st.title("Conversation Details")

    try:
        df = pd.read_csv(
            BASE_DIR/'data/conversationDetails.csv',
            delimiter="|",
            encoding="utf-8"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.write(f"Total Conversations: {len(df)}")

    except FileNotFoundError:
        st.error("CSV file not found.")
    except Exception as e:
        st.error(f"Error: {e}")
        
def eventDetails_UI():
    st.title("Event Details")

    try:
        df = pd.read_csv(
            BASE_DIR/'data/eventDetails.csv',
            delimiter="|",
            encoding="utf-8"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.write(f"Total Events: {len(df)}")

    except FileNotFoundError:
        st.error("CSV file not found.")
    except Exception as e:
        st.error(f"Error: {e}")