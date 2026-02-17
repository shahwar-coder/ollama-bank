'''
Cloud-Based LLM System (Why Internet is Required)

Flow:

User → (Query) → Cloud Server (LLM) → (Response) → User

Explanation:

1. The LLM is hosted in the cloud.
2. Your query must travel over the internet.
3. The cloud server processes it.
4. The response comes back over the internet.

Why Internet is Required:

- The model does NOT live on your machine.
- It lives on remote company servers.
- Every request = network call (API request).

If internet is down:
- You cannot send query.
- You cannot receive response.
- System stops working.

Simple Mental Model:

Cloud LLM = Brain on someone else's computer.
Internet = Bridge connecting you to that brain.
No bridge → No communication.
'''
