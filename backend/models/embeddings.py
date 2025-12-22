from sentence_transformers import SentenceTransformer

# Load once (important for performance)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
