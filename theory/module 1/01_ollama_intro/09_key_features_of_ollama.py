'''
Key Features of Ollama

1. Offline & Private by Default
   - Once a model is downloaded, it runs without internet.
   - Your data stays on your machine.
   - Ideal for personal, business, legal, or medical use cases.

2. Simple Installation & Setup
   - Download → Install → Done.
   - No complex ML environment setup.
   - No manual GPU driver configuration.
   - Beginner-friendly but powerful.

3. Easy Model Management (CLI-Based)
   - ollama pull llama3  → download model
   - ollama run llama3   → run model
   - ollama list         → view installed models
   - ollama rm llama3    → remove model

   Ollama handles model storage and lifecycle internally.

4. Pre-Built Model Library
   - Access to popular open-source models:
       Llama 3, Mistral, Gemma, Phi, Qwen, etc.
   - No need to manually download from multiple sources.
   - Like an "App Store" for LLMs.

5. Runs Multiple Models & Instant Switching
   - Install multiple models locally.
   - Switch instantly depending on task.
   - Compare outputs across models.
   - Use lightweight models for speed, larger models for reasoning.

6. Modelfile (Custom Model Configuration)
   - Create custom models using simple instructions.

     Example:
         FROM llama3
         PARAMETER temperature 0.3
         SYSTEM "You are a helpful AI tutor."

   - Set permanent system behavior.
   - Tune parameters.
   - Build domain-specific assistants.
   - No need to repeat prompts every time.

7. Integration with AI Ecosystem
   - Python SDK support.
   - REST API server built-in.
   - Works with LangChain, LlamaIndex.
   - Compatible with VS Code, PyCharm.
   - Runs on macOS, Windows, Linux.

   Enables transition from:
   "Local chatting"
   → to
   "Building production-grade AI systems."

8. Runs on Normal Hardware
   - Provides optimized/compressed model versions.
   - Works on standard laptops.
   - No expensive GPU required to start experimenting.

Summary:

Ollama = Private + Offline + Multi-Model + Customizable + Developer-Ready

It is not just a model runner.
It is a complete local LLM runtime for real AI engineering.
'''
