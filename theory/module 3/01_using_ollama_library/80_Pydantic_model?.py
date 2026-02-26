'''
Q1. What is a Pydantic model?

A.
A Pydantic model is a Python class that defines
structured data with built-in type checking and validation.
It ensures data follows a defined format.
'''
# Example:
# class User(BaseModel):
#     name: str
#     age: int



'''
Q2. Why do we inherit from BaseModel?

A.
Because BaseModel provides validation,
type enforcement, parsing, and serialization features.
Without it, the class is just a normal Python class.
'''
# Example:
# from pydantic import BaseModel
# class User(BaseModel):
#     name: str



'''
Q3. What does "data contract" mean in this context?

A.
It means the model defines strict rules
for what data is allowed.
Any data must follow those rules.
'''
# Example:
# name must be string
# age must be integer
# Otherwise → validation error



'''
Q4. How does Pydantic perform validation?

A.
When data is passed into the model,
Pydantic checks types and constraints automatically.
'''
# Example:
# User(name="John", age="25")
# age becomes int 25 (parsed automatically)



'''
Q5. What happens if invalid data is passed?

A.
Pydantic raises a validation error.
It prevents incorrect data from being accepted.
'''
# Example:
# User(name="John", age="abc")
# → ValidationError



'''
Q6. What is serialization in Pydantic?

A.
Serialization means converting the model
into standard formats like dict or JSON.
'''
# Example:
# user.dict()
# user.model_dump()  # in newer versions



'''
Q7. What is the core mental model of a Pydantic model?

A.
It is a structured, validated data container
that enforces correctness automatically.
'''
# Example:
# API request body
# Database schema representation
# LLM structured output parsing
