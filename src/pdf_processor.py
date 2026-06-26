from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF file.
    """
    reader = PdfReader(uploaded_file)

    document_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            document_text += text + "\n"

    return document_text