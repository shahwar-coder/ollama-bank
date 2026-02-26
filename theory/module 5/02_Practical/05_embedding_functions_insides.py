from langchain_ollama import OllamaEmbeddings

# instance
embedding_functions = OllamaEmbeddings(model="nomic-embed-text")

print(f"\nEmbedding Functions (TYPE):\n{type(embedding_functions)}")
print(f"\nEmbedding Functions:\n{embedding_functions}")
print(f"\nEmbedding Functions:\n{embedding_functions.model_dump_json()}")

# Embedding Functions (TYPE):
# <class 'langchain_ollama.embeddings.OllamaEmbeddings'>

# Embedding Functions:
# model='nomic-embed-text' validate_model_on_init=False base_url=None client_kwargs={} async_client_kwargs={} sync_client_kwargs={} mirostat=None mirostat_eta=None mirostat_tau=None num_ctx=None num_gpu=None keep_alive=None num_thread=None repeat_last_n=None repeat_penalty=None temperature=None stop=None tfs_z=None top_k=None top_p=None

# Embedding Functions:
# {
#   "model": "nomic-embed-text",
#   "validate_model_on_init": false,
#   "base_url": null,
#   "client_kwargs": {},
#   "async_client_kwargs": {},
#   "sync_client_kwargs": {},
#   "mirostat": null,
#   "mirostat_eta": null,
#   "mirostat_tau": null,
#   "num_ctx": null,
#   "num_gpu": null,
#   "keep_alive": null,
#   "num_thread": null,
#   "repeat_last_n": null,
#   "repeat_penalty": null,
#   "temperature": null,
#   "stop": null,
#   "tfs_z": null,
#   "top_k": null,
#   "top_p": null
# }

'''
OllamaEmbeddings JSON (Important fields only)

model
👉 Name of embedding model used
Example: "nomic-embed-text"
→ Converts text into vectors

validate_model_on_init
👉 Whether to check model availability during initialization
False → skip validation for faster startup

base_url
👉 Ollama server endpoint
None → uses default local Ollama server

client_kwargs
👉 Extra HTTP client settings (timeouts, headers)
Usually empty in local setup

num_ctx
👉 Context window size for model
Controls max tokens processed

num_gpu
👉 Number of GPUs to use
Relevant for hardware acceleration

num_thread
👉 CPU threads used for inference
Controls parallel compute usage

keep_alive
👉 Keeps model loaded in memory
Reduces reload latency

temperature
👉 Sampling randomness (mostly for generation models)
Not important for embeddings

top_k / top_p
👉 Sampling controls (generation-related)
Not relevant for embeddings

⭐ Key takeaway:
For embeddings, the most important fields are model, base_url, and hardware/runtime controls (num_gpu, num_thread, keep_alive).
'''