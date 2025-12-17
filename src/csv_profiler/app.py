import streamlit as st
import sys
import json
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from csv_profiler.io import parse_csv_string
from csv_profiler.profile import basic_profile
from csv_profiler.render import generate_markdown_report, generate_json_report


st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")


uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded:
    
    text = uploaded.getvalue().decode("utf-8")
    rows = parse_csv_string(text)
    st.write(f"**Loaded:** `{uploaded.name}` ({len(rows)} rows)")

    
    if st.button("Generate Profile"):
        with st.spinner("Analyzing..."):
            report = basic_profile(rows)
            st.session_state["report"] = report

    if "report" in st.session_state:
        report = st.session_state["report"]
        
        st.divider()
        st.subheader("Profiling Report")
        
        md_text = generate_markdown_report(report)
        st.markdown(md_text)
        
        st.divider()
        
        st.subheader("Downloads")
        col1, col2 = st.columns(2)
        
        json_text = generate_json_report(report)
        
        with col1:
            st.download_button(
                label="📥 Download JSON Report",
                data=json_text,
                file_name="report.json",
                mime="application/json"
            )
            
        with col2:
            st.download_button(
                label="📥 Download Markdown Report",
                data=md_text,
                file_name="report.md",
                mime="text/markdown"
            )

        with st.expander("View Raw JSON Data"):
            st.json(report)