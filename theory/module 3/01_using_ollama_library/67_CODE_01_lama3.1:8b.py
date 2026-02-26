import ollama

response = ollama.generate(
    model="llama3.1:8b",
    prompt="why are leaves of plant green in color?",
)

print(f"Response : {response}")

# In Terminal check : ollama list
# Choose model from list of downloaded models


'''
Response : model='llama3.1:8b' created_at='2026-02-25T21:44:02.745961Z' done=True done_reason='stop' total_duration=80804680917 load_duration=4695082583 prompt_eval_count=19 prompt_eval_duration=5145644084 eval_count=311 eval_duration=70029052696 response="Leaves appear green because they contain a pigment called chlorophyll, which plays a crucial role in photosynthesis. Chlorophyll is present in the cells of leaves and helps absorb light energy from the sun, which is then used to convert carbon dioxide and water into glucose and oxygen.\n\nChlorophyll absorbs blue and red light but reflects green light, which is why it appears green to our eyes. This process is called selective absorption, where certain wavelengths of light are absorbed while others are reflected or transmitted.\n\nHere's a simplified explanation:\n\n1.  **Light absorption:** Chlorophyll molecules absorb blue (400-500 nm) and red (600-700 nm) light from the sun.\n2.  **Reflectance:** The green light, which is between 520-560 nm, is not absorbed by chlorophyll but rather reflected back to our eyes.\n3.  **Appearance:** Since green light is reflected, it gives leaves their characteristic green color.\n\nAdditionally, other pigments like carotenoids and anthocyanins are also present in leaves. Carotenoids absorb blue and green light, while anthocyanins reflect red light. The combination of these pigments can result in a range of colors, from yellow to orange to purple, depending on the plant species.\n\n**Interesting fact:** Some plants have adapted to live in low-light environments, where chlorophyll's efficiency is reduced. In these cases, other pigments like anthocyanins become more prominent, leading to the development of red or purple leaves." thinking=None context=[128006, 882, 128007, 271, 35734, 527, 11141, 315, 6136, 6307, 304, 1933, 30, 128009, 128006, 78191, 128007, 271, 2356, 4798, 5101, 6307, 1606, 814, 6782, 264, 77678, 2663, 37833, 5237, 25734, 11, 902, 11335, 264, 16996, 3560, 304, 7397, 74767, 13, 92479, 5237, 25734, 374, 3118, 304, 279, 7917, 315, 11141, 323, 8779, 35406, 3177, 4907, 505, 279, 7160, 11, 902, 374, 1243, 1511, 311, 5625, 12782, 40589, 323, 3090, 1139, 34323, 323, 24463, 382, 1163, 9761, 5237, 25734, 91111, 6437, 323, 2579, 3177, 719, 27053, 6307, 3177, 11, 902, 374, 3249, 433, 8111, 6307, 311, 1057, 6548, 13, 1115, 1920, 374, 2663, 44010, 44225, 11, 1405, 3738, 93959, 315, 3177, 527, 42101, 1418, 3885, 527, 27000, 477, 34699, 382, 8586, 596, 264, 44899, 16540, 1473, 16, 13, 220, 3146, 14235, 44225, 68063, 92479, 5237, 25734, 35715, 35406, 6437, 320, 3443, 12, 2636, 26807, 8, 323, 2579, 320, 5067, 12, 7007, 26807, 8, 3177, 505, 279, 7160, 627, 17, 13, 220, 3146, 73889, 685, 68063, 578, 6307, 3177, 11, 902, 374, 1990, 220, 15830, 12, 17698, 26807, 11, 374, 539, 42101, 555, 37833, 5237, 25734, 719, 4856, 27000, 1203, 311, 1057, 6548, 627, 18, 13, 220, 3146, 30327, 68063, 8876, 6307, 3177, 374, 27000, 11, 433, 6835, 11141, 872, 29683, 6307, 1933, 382, 50674, 11, 1023, 24623, 1392, 1093, 1841, 66728, 17390, 323, 23064, 511, 8503, 1354, 527, 1101, 3118, 304, 11141, 13, 3341, 66728, 17390, 35406, 6437, 323, 6307, 3177, 11, 1418, 23064, 511, 8503, 1354, 8881, 2579, 3177, 13, 578, 10824, 315, 1521, 24623, 1392, 649, 1121, 304, 264, 2134, 315, 8146, 11, 505, 14071, 311, 19087, 311, 25977, 11, 11911, 389, 279, 6136, 9606, 382, 334, 85415, 2144, 68063, 4427, 11012, 617, 30464, 311, 3974, 304, 3428, 18179, 22484, 11, 1405, 37833, 5237, 25734, 596, 15374, 374, 11293, 13, 763, 1521, 5157, 11, 1023, 24623, 1392, 1093, 23064, 511, 8503, 1354, 3719, 810, 21102, 11, 6522, 311, 279, 4500, 315, 2579, 477, 25977, 11141, 13] logprobs=None
'''

# Understandinf code and response object:
'''
Ollama Python Inference – Detailed Explanation
=============================================

PART 1 — Understanding the Code
-------------------------------

import ollama

response = ollama.generate(
    model="llama3.1:8b",
    prompt="why are leaves of plant green in color?",
)

print(response)


1) import ollama
   - Imports the Ollama Python client.
   - This client communicates with the local Ollama server.
   - The server loads and runs the model on your machine.

   Architecture:
       Python Code
           ↓
       Ollama Client
           ↓
       Local Ollama Server
           ↓
       Model (GGUF in RAM)
           ↓
       Response Object


2) ollama.generate(...)
   - Sends a single prompt to the model.
   - This is stateless (no conversation memory unless manually passed).
   - Parameters:
        model  → Which local model to use
        prompt → Input text sent to model


------------------------------------------------------------------

PART 2 — Understanding the Response Object
-------------------------------------------

The response is NOT just text.
It contains metadata + performance details.

Example fields explained below.


1) model='llama3.1:8b'
   - Confirms which model generated the output.


2) created_at='timestamp'
   - Time when generation finished.


3) done=True
   done_reason='stop'
   - Model completed normally.
   - It stopped because it reached a stop token.
   - Other possible reasons:
        "length"  → hit max token limit
        "error"
        "cancelled"


------------------------------------------------------------------

PART 3 — Performance Metrics (Very Important)
---------------------------------------------

All duration values are in nanoseconds.

1) total_duration
   - Total time for full request.
   - Includes:
        model loading
        prompt evaluation
        token generation

2) load_duration
   - Time to load model into memory.
   - Happens:
        first run
        or after model was unloaded

3) prompt_eval_count
   - Number of input tokens.
   - Your question became 19 tokens.

4) prompt_eval_duration
   - Time taken to process input tokens.

5) eval_count
   - Number of output tokens generated.
   - In your case: 311 tokens.

6) eval_duration
   - Time taken to generate output tokens.
   - This is usually the most expensive part.


------------------------------------------------------------------

PART 4 — The "response" Field
------------------------------

response["response"]

This contains the actual human-readable answer generated by the model.

Example:
    "Leaves appear green because..."


------------------------------------------------------------------

PART 5 — The "context" Field
----------------------------

context=[128006, 882, 128007, ...]

This is:
    The tokenized form of the conversation.

Each number = token ID.

The model does NOT see words.
It sees token IDs.

Normally you do not need to use this unless:
    - Building advanced multi-turn systems
    - Managing manual context


------------------------------------------------------------------

PART 6 — Why It Took ~80 Seconds
--------------------------------

Machine:
    M1 MacBook Air
    8GB RAM
    CPU inference

Model:
    8B parameters

Generated:
    311 tokens

Larger model + long output = slower generation.

If you use:
    llama3.2:1b

It will be significantly faster.


------------------------------------------------------------------

PART 7 — Cleaner Way to Print Output
-------------------------------------

Instead of printing the whole object:

    print(response["response"])

This prints only the model's answer.


------------------------------------------------------------------

PART 8 — What You Just Observed (Inference Lifecycle)
-----------------------------------------------------

Complete LLM inference process:

    1) Model load
    2) Prompt tokenization
    3) Prompt evaluation
    4) Token-by-token generation
    5) Stop token detection
    6) Return response + metadata


------------------------------------------------------------------

KEY ENGINEERING INSIGHTS
------------------------

- Token count affects speed.
- Model size affects latency.
- Output length affects generation time.
- Model load time happens once per session.
- Performance metrics are critical for optimization.

You are now looking at inference like a systems engineer,
not just as a user.
'''