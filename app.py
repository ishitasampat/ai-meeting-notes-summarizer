import streamlit as st
from summarizer import summarize_meeting
from pdf_reader import extract_text_from_pdf

st.set_page_config(
    page_title="Meeting Intelligence Platform",
    page_icon="📋",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("📋 Meeting Intelligence")
    st.markdown("---")

    st.markdown("### Supported Files")
    st.write("✅ TXT")
    st.write("✅ PDF")

    st.markdown("---")

    st.info(
        "Upload meeting transcripts to generate structured business insights."
    )

# Main page
st.title("📋 Meeting Intelligence Platform")
st.subheader(
    "Transform meeting transcripts into actionable business insights."
)

uploaded_file = st.file_uploader(
    "Upload Meeting Transcript",
    type=["txt", "pdf"]
)

if uploaded_file:

    if uploaded_file.type == "application/pdf":
        transcript = extract_text_from_pdf(uploaded_file)
    else:
        transcript = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Transcript Preview")

    st.text_area(
        "Meeting Transcript",
        transcript,
        height=250,
        key="transcript_preview"
    )

    if st.button("🚀 Generate Meeting Intelligence"):

        with st.spinner("Analyzing meeting..."):

            result = summarize_meeting(transcript)

        # Dashboard Metrics
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Documents Processed", "1")
        col2.metric("Supported Formats", "2")
        col3.metric("AI Engine", "Gemini")
        col4.metric("Status", "Complete")

        st.markdown("---")

        st.subheader("📊 Generated Meeting Intelligence")

        st.markdown(result)

        st.download_button(
            label="📥 Download Meeting Report",
            data=result,
            file_name="meeting_report.md",
            mime="text/markdown"
        )