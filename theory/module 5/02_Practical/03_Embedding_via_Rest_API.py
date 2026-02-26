import requests
import json

text_to_embed = "The sun is the center of our solar system."

url = "http://localhost:11434/api/embeddings"

payload = {
    "model" : "nomic-embed-text",
    "prompt" : text_to_embed
}

response = requests.post(url, json=payload)
# print(response) # <Response [200]>

data = response.json()
embedding = data.get("embedding")
print(f"Embeddings (First 10):\n{embedding[:10]}")
print(f"Length of Embeddings:\n{len(embedding)}")


# Embeddings (First 10):
# [0.5617655515670776, 1.0531878471374512, -3.035295009613037, -0.030941616743803024, 0.16354578733444214, 0.5733382701873779, 0.10614123195409775, -1.6527913808822632, 0.9216956496238708, -1.0621384382247925]
# Length of Embeddings:
# 768