import ollama
import json

messages = [
    {
        "role": "system",
        "content": "You are a JSON generator. Always return valid JSON only."
    },
    {
        "role": "user",
        "content": """
Return JSON with fields:
{
  "name": string,
  "age": number
}

Person: Elon Musk
"""
    }
]

response = ollama.chat(
    model='llama3',
    messages=messages,
    format='json'
)

# raw json string
json_text = response['message']['content']

# convert to python dict
data = json.loads(json_text)

print("Parsed object:", data)
print("Name:", data["name"])
print("Age:", data["age"])


# =/=/=/==/=/=/==/=/=/==/=/=/==/=/=/==/=/=/==/=/=/=


'''
Q1. What problem does format='json' solve?

A.
Normally, LLMs return natural language text.
That text is hard to reliably parse in programs.
format='json' forces the output to be valid JSON,
which is machine-readable.
'''
# Example:
# Without JSON:
# "Name: John\nAge: 25"
# With JSON:
# {"name": "John", "age": 25}



'''
Q2. What exactly does format='json' guarantee?

A.
It guarantees that the output will be valid JSON.
It does NOT guarantee correct schema or field names.
'''
# Example:
# Valid JSON but wrong schema:
# {"full_name": "John"}  # Still valid JSON



'''
Q3. Why is JSON output important for agents?

A.
Because agents need structured data
to make decisions, call tools, or trigger workflows.
'''
# Example:
# data = {"age": 52}
# if data["age"] > 50:
#     call_health_tool()



'''
Q4. Does format='json' automatically define structure?

A.
No.
You must clearly define the expected structure in the prompt.
'''
# Example:
# Prompt:
# Return JSON with fields:
# {
#   "name": string,
#   "age": number
# }



'''
Q5. What is the professional pattern for reliable JSON generation?

A.
1. Add system message: "Always return valid JSON."
2. Clearly define expected fields in prompt.
3. Use format='json'.
4. Parse using json.loads().
'''
# Example:
# json_text = response['message']['content']
# data = json.loads(json_text)



'''
Q6. What is the mental model difference?

A.
Without format:
LLM → natural language generator

With format:
LLM → constrained JSON generator
'''
# Example:
# format=None → paragraph explanation
# format='json' → structured object



'''
Q7. How does structured output enable automation?

A.
It allows programmatic control.
Python can read keys and take actions automatically.
'''
# Example:
# {"action": "send_email"}
# → Python calls email function



'''
Q8. What are the levels of structured output maturity?

A.
Level 1 → JSON mode (valid JSON)
Level 2 → JSON schema enforcement
Level 3 → Tool/function calling
'''
# Example:
# Level 1 → format='json'
# Level 3 → Model selects tool + arguments



'''
Q9. What is the final core intuition?

A.
format='json' turns LLM output
into something programs can reliably use.
It is the bridge between reasoning and execution.
'''
# Example:
# User → LLM → JSON decision → Python executes tool
