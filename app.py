import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="PlantMind AI")

st.title("🏭 PlantMind AI")
st.subheader("Industrial Knowledge Copilot")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    document_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            document_text += text

    st.success("Document processed successfully!")

    if st.button("Generate Summary"):

        summary_prompt = f"""
        Summarize this industrial document in simple bullet points:

        {document_text}
        """

        summary = model.generate_content(summary_prompt)

        st.subheader("Document Summary")

        st.write(summary.text)

    question = st.text_input(
        "Ask a question about this document"
    )

    if question:

        prompt = f"""
        You are an industrial knowledge assistant.

        Use only the information below.

        DOCUMENT:
        {document_text}

        QUESTION:
        {question}

        ANSWER:
        """

        response = model.generate_content(prompt)

        st.subheader("Answer")

        st.write(response.text)
        # INCIDENT ANALYSIS

st.subheader("Incident Analysis")

incident = st.text_area(
    "Describe an industrial incident"
)

if st.button("Analyze Incident"):

    incident_prompt = f"""
    You are an industrial safety expert.

    Based on the uploaded document:

    {document_text}

    Analyze the following incident:

    {incident}

    Provide:

    1. Possible Causes
    2. Risks
    3. Recommended Actions
    """

    result = model.generate_content(
        incident_prompt
    )

    st.write(result.text)