def summary_prompt(document_text):
    return f"""
Summarize this industrial document in simple bullet points.

DOCUMENT:
{document_text}
"""


def question_prompt(document_text, question):
    return f"""
You are an industrial knowledge assistant.

Use only the information below.

DOCUMENT:
{document_text}

QUESTION:
{question}

ANSWER:
"""


def rag_question_prompt(context, question):
    return f"""
You are an industrial knowledge assistant.

Answer the question using ONLY the context below.

If the answer is not present in the context, reply:

"I could not find that information in the uploaded document."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""


def incident_prompt(document_text, incident):
    return f"""
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