import streamlit as st
import requests

st.title("AI Research Agent")
st.subheader("Generate research reports from the web using Groq API.")

query = st.text_input("Enter research topic:")

if st.button("Generate Report"):
    if query:
        st.info("Generating report...")
        try:
            response = requests.post("http://localhost:8000/generate", json={"query": query})
            if response.status_code == 200:
                data = response.json()
                report_url = data.get("url")
                st.success("Report generated!")
                preview = requests.get("http://localhost:8000/preview").json().get("content", "No preview available.")
                st.markdown("### Preview:")
                st.text_area("Report Content:", preview, height=300)
                st.markdown(f"[Download Report]({report_url})")
            else:
                st.error("Failed to generate report. Please try again.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
