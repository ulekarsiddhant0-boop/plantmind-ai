import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def chunk_text(text, chunk_size=500):
    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def create_index(chunks):

    embeddings = embedding_model.encode(chunks)

    index = faiss.IndexFlatL2(
        embeddings.shape[1]
    )

    index.add(
        np.array(embeddings).astype("float32")
    )

    return index, chunks


def retrieve(query, index, chunks, k=3):

    query_embedding = embedding_model.encode(
        [query]
    )

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    return [
        chunks[i]
        for i in indices[0]
    ]