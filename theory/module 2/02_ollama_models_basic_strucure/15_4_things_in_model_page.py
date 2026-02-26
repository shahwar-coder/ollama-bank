'''
When you open a model page in Ollama,
you usually see 4 sections:

1️⃣ model
2️⃣ license
3️⃣ params
4️⃣ template

Here’s what each means:

--------------------------------------------------

1️⃣ model

This is the actual model file information.

It shows:
- Architecture (e.g., llama)
- Parameter size (e.g., 8B)
- Quantization type (e.g., Q4_K_M)
- File size (e.g., 4.9GB)

👉 This is the real GGUF model that runs on your machine.
It contains the trained weights (brain of the model).

--------------------------------------------------

2️⃣ license

This tells you:
- Who owns the model
- Whether you can use it commercially
- Any restrictions

Example:
"Llama 3.1 Community License"

👉 Always check this if you plan to use the model in production.

--------------------------------------------------

3️⃣ params

These are default runtime parameters.

Example:
{
  "stop": ["<|start_header_id|>", "<|end_header_id|>", "<|eot_id|>"]
}

They define:
- Stop tokens
- Generation behavior defaults
- Sometimes temperature or system-level rules

👉 Think of this as default generation settings.

--------------------------------------------------

4️⃣ template

This is the prompt format wrapper.

It defines how your input is structured before sending to the model.

Example (simplified idea):
System:
User:
Assistant:

It ensures:
- Proper role formatting
- Chat-style interaction
- Tool-calling compatibility

👉 This is extremely important.
If template is wrong, model responses break.

--------------------------------------------------

Simple Analogy:

model     → The brain (weights file)
license   → The legal contract
params    → Default behavior settings
template  → The conversation format structure

--------------------------------------------------

Big Insight:

Ollama is not just storing a raw model.

It stores:
✓ The model
✓ The legal metadata
✓ The default runtime config
✓ The chat formatting logic

That’s why it works smoothly out of the box.
'''