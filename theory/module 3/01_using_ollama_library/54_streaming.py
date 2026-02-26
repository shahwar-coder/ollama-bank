import ollama

stream = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': 'Explain RAG'}],
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)


# =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=


'''
Q1. What does setting stream=True do in ollama.chat()?

A.
It enables streaming mode.
The model sends output token-by-token instead of waiting for the full response.
'''
# Example:
# Without stream → Full paragraph appears at once
# With stream → Text appears gradually in real time



'''
Q2. What is returned when stream=True is used?

A.
Instead of a single dictionary,
it returns an iterable stream of chunks.
Each chunk contains partial generated text.
'''
# Example:
# for chunk in stream:
#     print(chunk)



'''
Q3. Why do we loop over "for chunk in stream"?

A.
Because the model sends small pieces of text continuously.
We must collect and print them as they arrive.
'''
# Example:
# chunk1 → "Retrieval"
# chunk2 → " Augmented"
# chunk3 → " Generation"



'''
Q4. Why do we use end='' in print()?

A.
To avoid adding a newline after every chunk.
This keeps the text flowing naturally.
'''
# Example:
# print(text, end='')
# Output appears like a normal paragraph



'''
Q5. Why is flush=True important?

A.
It forces Python to immediately display each chunk.
Without it, output may buffer and appear delayed.
'''
# Example:
# flush=True → Instant display
# No flush → Delayed output



'''
Q6. Why is streaming critical for UI applications?

A.
Because users prefer real-time feedback.
It improves responsiveness and user experience.
'''
# Example:
# Chatbot UI typing effect
# Live answer generation
# AI assistant interfaces



'''
Q7. What is the core mental model of streaming?

A.
Normal mode → Wait → Full response.
Streaming mode → Receive tokens → Display instantly.
'''
# Example:
# stream=True → Token flow
# stream=False → Complete text after processing
