from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user1 = User(name="Ashok", age=25)
user2 = User(name="Rahul", age="25")
# user3 = User(name="Rahul", age="twenty-five")

print(f"User 1 : {user1}")
print(f"User 2 : {user2}")
# print(f"User 3 : {user3}")

# Output for Usr 1 nd User 2:
# User 1 : name='Ashok' age=25
# User 2 : name='Rahul' age=25

# But for User 3...
# ValidationError will be raised
# because "twenty-five" cannot be converted to int.
#
# Pydantic tries automatic type coercion (e.g., "25" → 25),
# but fails when conversion is not possible.
#
# So uncommenting user3 will produce:
# pydantic.ValidationError: Input should be a valid integer


# /=/=/=/=/=/=/=/=/=/=/=/=/==/=/=/=/=/=/==/=/=/=/==/=/=/=/==/=/=/=/


'''
PYDANTIC TYPE COERCION & VALIDATION — SUMMARY
=============================================

1️⃣ What is happening here?
- User inherits from BaseModel → Pydantic model
- Pydantic performs:
    ✔ validation
    ✔ parsing
    ✔ type coercion

So model creation is NOT plain object construction.

--------------------------------------------------

2️⃣ user1 → already valid types
User(name="Ashok", age=25)

- name → str ✅
- age → int ✅
- Stored as-is

--------------------------------------------------

3️⃣ user2 → automatic coercion
User(name="Rahul", age="25")

- age expected → int
- received → str "25"
- Pydantic attempts parsing
- Conversion succeeds → 25

👉 This is called TYPE COERCION (or parsing)

So object becomes:
User(name='Rahul', age=25)

--------------------------------------------------

4️⃣ user3 → validation failure
User(name="Rahul", age="twenty-five")

- age expected → int
- received → non-numeric string
- Conversion impossible

👉 Pydantic raises ValidationError

This is SAFE failure.

--------------------------------------------------

5️⃣ Mental model (VERY important)
Plain Python class:
    constructor stores values blindly

Pydantic model:
    constructor = validate + parse + store

So creation itself enforces schema.

--------------------------------------------------

6️⃣ Backend engineering insight
Why this is powerful:

✔ protects API boundaries
✔ normalizes incoming data
✔ prevents invalid state
✔ reduces manual validation code
✔ guarantees downstream assumptions

This is why FastAPI, AI SDKs, configs, etc. rely heavily on Pydantic.

--------------------------------------------------

👉 One-liner to remember
Pydantic models are "self-validating objects".
'''