import streamlit as st
from summarizer import summarize_meeting

st.set_page_config(
    page_title="AI Meeting Notes Summarizer",
    page_icon="📝"
)

st.title("📝 AI Meeting Notes Summarizer")

uploaded_file = st.file_uploader(
    "Upload Meeting Transcript",
    type=["txt"]
)

if uploaded_file:

    transcript = uploaded_file.read().decode("utf-8")

    st.subheader("Transcript Preview")

    st.text_area(
        "Meeting Transcript",
        transcript,
        height=250
    )

    if st.button("Generate Summary"):

        with st.spinner("Analyzing meeting..."):

            result = summarize_meeting(transcript)

        st.subheader("Generated Meeting Notes")

        st.markdown(result)