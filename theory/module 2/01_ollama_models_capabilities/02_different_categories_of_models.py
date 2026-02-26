'''
Ollama Model Categories (With Examples)

These are model categories in the Ollama library.
They group models based on capability and use case.

--------------------------------------------------

1️⃣ Cloud
   - Hosted / hybrid-access models.
   - May require internet.
   - Designed for large-scale or enterprise use.

   Example:
   - glm-5
   - minimax-m2.5

--------------------------------------------------

2️⃣ Embedding
   - Convert text → numerical vectors.
   - Used for RAG, semantic search, similarity matching.
   - Do NOT generate chat responses.

   Example:
   - nomic-embed-text
   - mxbai-embed-large

--------------------------------------------------

3️⃣ Vision
   - Multimodal models (text + image).
   - Can analyze images and answer questions.

   Example:
   - llava
   - qwen2.5-vl
   - llama3.2-vision

--------------------------------------------------

4️⃣ Tools
   - Optimized for function/tool calling.
   - Return structured JSON outputs.
   - Useful for AI agents & automation.

   Example:
   - llama3 (tool-enabled variants)
   - qwen2.5 (tool-capable versions)

--------------------------------------------------

5️⃣ Thinking
   - Strong reasoning & multi-step logic models.
   - Better for math, planning, deep analysis.

   Example:
   - qwen3.5
   - lfm2.5-thinking
   - deepseek-r1

--------------------------------------------------

Important:

These are capability categories.
All models still run via the same Ollama runtime.

Quick Mental Map:

Cloud      → Remote large models
Embedding  → Text → Vector
Vision     → Image + Text
Tools      → Function calling
Thinking   → Deep reasoning
'''
