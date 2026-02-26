'''
Steps I Followed to Install and Run a Model using Ollama

1. Install Ollama
   - Download from ollama.com
   - Install on system (Mac in this case)

2. Open Terminal

3. Run the Model Command

   ollama run llama3.1:8b

4. What Happened Internally

   - Ollama started pulling model layers
   - Downloaded multiple blobs (model weights)
   - Verified SHA256 digest
   - Wrote model manifest
   - Installation completed successfully

5. Model Ready to Use

   - Prompt appeared:
       >>> Who is PM of India?

   - Model generated a response.
   - Model now runs locally on my system.

Important Understanding:

- First run → Downloads model (~4–5GB).
- After download → Works offline.
- Model is stored locally (~/.ollama/models).
- No cloud API used.
- No per-token payment.

Simple Flow:

Install Ollama
→ Run ollama run model-name
→ Model downloads
→ Model runs locally
→ Start chatting

This confirms successful local LLM setup.
'''
