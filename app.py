import streamlit as st
from csv_profiler.io import parse_csv_string
from csv_profiler.profile import basic_profile

st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")

uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded:

    text = uploaded.getvalue().decode("utf-8")
    rows = parse_csv_string(text)
    
    st.write(f"Parsed {len(rows)} rows.")

    
    if st.button("Generate Profile"):

        profile = basic_profile(rows)
        st.session_state["profile"] = profile


    if "profile" in st.session_state:
        profile = st.session_state["profile"]
        
    
        st.write("### Summary")
        st.write(f"Rows: {profile['rows']}")
        st.write(f"Columns: {profile['n_cols']}")
        
        st.write("### Raw Profile Data")
        
        st.write(profile)