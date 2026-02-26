'''
Vision Capability & Multimodal Models – Clear Summary

1️⃣ What is Vision Capability?

Vision capability means:
The LLM can understand and reason over images,
not just text.

It can:
✓ Describe images
✓ Answer questions about images
✓ Extract text (OCR-like)
✓ Analyze charts/diagrams
✓ Interpret screenshots


--------------------------------------------------

2️⃣ What is Multimodal?

Multimodal = More than one type of input.

Traditional LLM:
    Input → Text only

Vision Model:
    Input → Text + Image

Example:

Input:
    [Image of receipt] + "What is the total amount?"

Model:
    Reads image → Extracts numbers → Answers


--------------------------------------------------

3️⃣ How It Works (Conceptually)

Image
   ↓
Converted into embeddings (numerical vectors)
   ↓
Combined with text embeddings
   ↓
Processed by multimodal transformer
   ↓
Generates text output


--------------------------------------------------

4️⃣ Why Vision Matters

Extends capability beyond text:

✓ Document understanding
✓ UI automation (read screenshots)
✓ Medical image analysis (assistive)
✓ Industrial inspection
✓ Education tools
✓ Real-world AI agents


--------------------------------------------------

5️⃣ Example in Ollama

Vision-capable models:

- llava
- llama3.2-vision
- qwen2.5-vl

These models accept:

    Image + Prompt

Example:

    "Describe this image."

Or:

    "What error message is shown in this screenshot?"


--------------------------------------------------

6️⃣ Big Picture

Text-only LLM:
    Reads → Thinks → Responds

Vision LLM:
    Sees → Reads → Thinks → Responds

--------------------------------------------------

One-Line Summary:

Vision capability = Multimodal LLM
that can understand images along with text.
'''
