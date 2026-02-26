from langchain_ollama import OllamaEmbeddings

# instance
embedding_functions = OllamaEmbeddings(model="nomic-embed-text")

# query text
query_text = "What is the largest planet"

# query embedding
query_embedding = embedding_functions.embed_query(query_text)

print(len(query_embedding))
print(query_embedding[:10])

# 768
# [-0.0025496874, 0.111298256, -0.13881871, 0.0014372517, 0.016813967, 0.07597, -0.038180076, -0.0011551637, -0.01893986, -0.049634084]