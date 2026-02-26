import ollama

messages = [
    {'role': 'system', 'content': 'You are helpful'}
]

messages.append({'role': 'user', 'content': 'What is attention?'})

response = ollama.chat(model='llama3', messages=messages)

messages.append(response['message'])

messages.append({'role': 'user', 'content': 'Give example'})

# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=

'''
Q1. Who is responsible for maintaining conversation history in Ollama?

A.
You (the developer) are responsible for maintaining the conversation history.
Ollama does not automatically remember previous messages.
'''
# Example:
# messages = []
# You keep appending user and assistant messages manually



'''
Q2. Why do we append response['message'] back to the messages list?

A.
Because the model’s reply must become part of the conversation history.
Without adding it, the model will not remember what it previously said.
'''
# Example:
# messages.append(response['message'])
# Now the assistant’s reply is stored for the next turn



'''
Q3. What happens if we do not store previous messages?

A.
The model will treat every request as a new conversation.
It will not remember earlier questions or answers.
'''
# Example:
# Ask: "What is attention?"
# Then ask: "Give example"
# Without history → Model won’t know example of what



'''
Q4. Why is a system message usually added first?

A.
Because it sets the behavior or rules for the entire conversation.
It acts like initial instructions.
'''
# Example:
# {'role': 'system', 'content': 'You are helpful'}
# Model stays helpful throughout conversation



'''
Q5. What is the core mental model of multi-turn chat in Ollama?

A.
Ollama generates responses based only on the messages you send.
If you want memory, you must send full conversation history each time.
'''
# Example:
# Turn 1 → send messages list
# Turn 2 → send updated messages list
# Each call includes complete history



'''
Q6. Why do we say "You manage memory"?

A.
Because the conversation state lives inside your Python variable (messages).
Ollama is stateless between requests.
'''
# Example:
# If program restarts,
# messages list is gone
# Conversation memory is lost
