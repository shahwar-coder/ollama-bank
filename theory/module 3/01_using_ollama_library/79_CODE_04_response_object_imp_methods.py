import ollama
import json
from pprint import pprint

print("\n=== 🔹 Generating response ===")

response = ollama.generate(
    model="llama3.2:1b",
    prompt="why are leaves green"
)

# -------------------------------------------------
print("\n=== 🔹 1. Response TYPE ===")
print(type(response))

# -------------------------------------------------
print("\n=== 🔹 2. Model fields (schema) ===")
pprint(type(response).model_fields.keys())

# -------------------------------------------------
print("\n=== 🔹 3. Convert to dict ===")
data = response.model_dump()
pprint(data.keys())

print("\nResponse text:")
print(data["response"])

# -------------------------------------------------
print("\n=== 🔹 4. Convert to JSON ===")
json_text = response.model_dump_json()
print(json_text[:200], "...")  # preview

# -------------------------------------------------
print("\n=== 🔹 5. Create COPY ===")
copy_resp = response.model_copy()

print("Original id:", id(response))
print("Copy id    :", id(copy_resp))
print("Same object?", response is copy_resp)

# -------------------------------------------------
print("\n=== 🔹 6. Compare content equality ===")
print("Same content?", response.model_dump() == copy_resp.model_dump())


# =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=

# OUTPUT

# === 🔹 Generating response ===

# === 🔹 1. Response TYPE ===
# <class 'ollama._types.GenerateResponse'>

# === 🔹 2. Model fields (schema) ===
# dict_keys(['model', 'created_at', 'done', 'done_reason', 'total_duration', 'load_duration', 'prompt_eval_count', 'prompt_eval_duration', 'eval_count', 'eval_duration', 'response', 'thinking', 'context', 'logprobs'])

# === 🔹 3. Convert to dict ===
# dict_keys(['model', 'created_at', 'done', 'done_reason', 'total_duration', 'load_duration', 'prompt_eval_count', 'prompt_eval_duration', 'eval_count', 'eval_duration', 'response', 'thinking', 'context', 'logprobs'])

# Response text:
# Leaves appear green because of the presence of a pigment called chlorophyll. Chlorophyll is a green compound that plays a crucial role in photosynthesis, the process by which plants convert sunlight, water, and carbon dioxide into glucose and oxygen.

# Chlorophyll absorbs light most efficiently in the red and blue parts of the visible spectrum, but reflects light in the green part of the spectrum, which is why it appears green to our eyes. This is known as the "chlorophyll-a" pigment, and it's responsible for the green coloration of leaves.

# There are two types of chlorophyll: chlorophyll a and chlorophyll b. Chlorophyll a is the most common form and absorbs light most efficiently in the red and blue parts of the spectrum. It's also the primary pigment responsible for photosynthesis.

# Leaves that lack chlorophyll, such as those found on some types of algae or aquatic plants, may appear yellow, orange, or brown. This is because these pigments are more efficient at absorbing light in other parts of the visible spectrum, allowing them to capture more energy from the sun and survive without photosynthesis.

# It's worth noting that leaves can also develop various pigments over time due to factors such as age, environmental conditions, and disease. For example, some trees may develop a reddish tint on their leaves during the fall season due to the accumulation of anthocyanins, which are responsible for the red, purple, and blue colors found in many fruits and flowers.

# Overall, the green coloration of leaves is an essential characteristic that helps plants survive and thrive by facilitating photosynthesis.

# === 🔹 4. Convert to JSON ===
# {"model":"llama3.2:1b","created_at":"2026-02-26T07:30:40.110512Z","done":true,"done_reason":"stop","total_duration":11031379875,"load_duration":1890078125,"prompt_eval_count":29,"prompt_eval_duration" ...

# === 🔹 5. Create COPY ===
# Original id: 4409780544
# Copy id    : 4409782144
# Same object? False

# === 🔹 6. Compare content equality ===
# Same content? True


'''
OLLAMA PYTHON RESPONSE OBJECT — SUMMARY
=======================================

1️⃣ Response type
- ollama.generate() does NOT return a dict.
- It returns a structured object (GenerateResponse).
- This object is a Pydantic model instance.

2️⃣ Schema inspection
- type(response).model_fields shows the schema.
- Useful for understanding available metadata fields.

3️⃣ Convert to dict
- response.model_dump() → plain Python dict.
- Used for logging, storage, and downstream processing.

4️⃣ Convert to JSON
- response.model_dump_json() → JSON string.
- Used for API responses, message queues, file logging.
- Avoid manual json.dumps(model_dump()).

5️⃣ Copying response
- response.model_copy() → new object with same content.
- Memory different, content same.
- Useful to avoid mutation side effects.

6️⃣ Equality vs identity
- response is copy_resp → False (different objects)
- response.model_dump() == copy_resp.model_dump() → True (same data)

🔥 Core backend insight
Modern AI SDK pattern:
API → JSON → SDK → Pydantic model → Developer

So developers work with:
- typed attributes
- validation
- schema guarantees
- clean serialization methods

🧠 Mental model to remember
response.model            → attribute access
response.model_dump()     → dict view
response.model_dump_json()→ JSON view
response.model_copy()     → object clone
response.model_fields     → schema

This pattern appears across OpenAI, Anthropic, Ollama, etc.
'''