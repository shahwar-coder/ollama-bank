'''
Concise Flow: How Ollama Works (Step-by-Step)

1. Download & Install Ollama
   - Install Ollama on your system.

2. Pull a Model
   - Example: ollama pull llama3
   - Model (GGUF format) is downloaded.
   - Stored locally (~/.ollama/models).

3. Model Loads into Memory
   - When you run it, model loads into RAM.
   - Uses CPU (or GPU if available).

4. Send Prompt
   - User types a prompt.
   - Ollama passes prompt to the model.

5. Inference Happens
   - Model processes input.
   - Generates tokens (response).

6. Output Returned
   - Response sent back to user.

Simple Flow:

Install → Download Model → Load into Memory → Prompt → Inference → Response
'''
