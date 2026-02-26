'''
Q1. Why do real systems need structured data validation?

A.
Because data flowing through systems is often messy,
untyped, or inconsistent.
Without validation, errors can silently propagate.
'''
# Example:
# API sends {"age": "twenty"}
# Without validation → crash later
# With validation → immediate error



'''
Q2. How does Pydantic act as a gatekeeper?

A.
Pydantic validates incoming data before it is used.
If data is incorrect, it raises an error.
If valid, it converts it into a safe Python object.
'''
# Example:
# Input: {"age": "25"}
# Output: age = 25 (converted to int)



'''
Q3. Where is Pydantic commonly used?

A.
It is used in APIs, databases, message queues,
and LLM output parsing.
Anywhere structured data must be trusted.
'''
# Example:
# FastAPI request body validation
# Parsing LLM JSON output safely



'''
Q4. What problem happens without validation?

A.
Incorrect data may pass through the system
and cause bugs in unexpected places.
'''
# Example:
# age expected int
# received string
# later arithmetic operation fails



'''
Q5. What is the flow when using Pydantic?

A.
Incoming data → validation → parsed model → safe usage.
'''
# Example:
# raw_json → UserModel(**raw_json) → validated object



'''
Q6. What is the core mental model of Pydantic?

A.
Pydantic = structured gatekeeper.
Only valid, correctly typed data is allowed inside.
'''
# Example:
# Bad data → rejected
# Good data → clean Python object
