'''
When You Download a Model in Ollama (macOS)

1. Where is the model stored?

On macOS, models are stored in:

    ~/.ollama/models

This directory contains:
- Model manifests
- Blob files (actual model weights)
- Metadata


2. What format is the model saved in?

Most Ollama models are stored in:

    GGUF format

(GGUF = GPT-Generated Unified Format)


3. What does GGUF mean?

GGUF is a binary format designed for:

- Efficient local inference
- Quantized models (smaller size, faster)
- Running on CPUs and GPUs
- Optimized loading into memory

It is commonly used by:
- llama.cpp ecosystem
- Local LLM runtimes (including Ollama)


Simple Understanding:

When you run:

    ollama pull llama3

Ollama:
- Downloads the model in GGUF format
- Stores it in ~/.ollama/models
- Prepares it for local execution

So:

Download → Stored locally → GGUF file → Loaded into memory → Used for inference
'''
