import streamlit as st

from src.pdf_processor import extract_text_from_pdf
from src.llm import model
from src.rag import (
    chunk_text,
    create_index,
    retrieve,
)
from src.prompts import (
    summary_prompt,
    rag_question_prompt,
    incident_prompt,
)

st.set_page_config(page_title="PlantMind AI")

st.title("🏭 PlantMind AI")
st.subheader("Industrial Knowledge Copilot")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

document_text = ""
chunks = []
index = None

if uploaded_file:

    document_text = extract_text_from_pdf(uploaded_file)

    chunks = chunk_text(document_text)

    index, chunks = create_index(chunks)

    st.success("Document processed successfully!")

    if st.button("Generate Summary"):

        summary = model.generate_content(
            summary_prompt(document_text)
        )

        st.subheader("Document Summary")
        st.write(summary.text)

    question = st.text_input(
        "Ask a question about this document"
    )

    if question:

        retrieved_chunks = retrieve(
            question,
            index,
            chunks
        )

        context = "\n\n".join(retrieved_chunks)

        response = model.generate_content(
            rag_question_prompt(
                context,
                question
            )
        )

        st.subheader("Answer")
        st.write(response.text)

        with st.expander("Retrieved Context"):
            st.write(context)

st.subheader("Incident Analysis")

incident = st.text_area(
    "Describe an industrial incident"
)

if st.button("Analyze Incident"):

    if not document_text:
        st.warning(
            "Please upload a PDF before analyzing an incident."
        )

    elif not incident.strip():
        st.warning(
            "Please describe the incident."
        )

    else:

        result = model.generate_content(
            incident_prompt(
                document_text,
                incident
            )
        )

        st.subheader("Incident Analysis Result")
        st.write(result.text)