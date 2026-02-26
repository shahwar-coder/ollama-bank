'''
Q1. What does num_predict control?

A.
num_predict controls the maximum number of tokens
the model is allowed to generate in its response.
'''
# Example:
# num_predict=50 → Short reply
# num_predict=500 → Detailed explanation



'''
Q2. Is num_predict the same as max_tokens?

A.
Yes.
num_predict is equivalent to max_tokens in other APIs.
Both limit output length.
'''
# Example:
# OpenAI → max_tokens=200
# Ollama → num_predict=200



'''
Q3. What happens if num_predict is too small?

A.
The response may be cut off before completing.
It may end mid-sentence.
'''
# Example:
# num_predict=10
# Output: "Transformers are neural networks that..."



'''
Q4. What happens if num_predict is very large?

A.
The model can generate longer responses,
but it will still stop when it finishes naturally.
'''
# Example:
# num_predict=1000
# Model may stop at 300 tokens if answer is complete



'''
Q5. Why must num_predict fit inside the context window?

A.
Because total tokens = input tokens + generated tokens.
Both must stay within the model’s context limit.
'''
# Example:
# Context = 8192
# Input = 8000
# num_predict cannot exceed ~192 tokens



'''
Q6. What is the simple mental model for num_predict?

A.
num_predict = maximum output length allowed.
'''
# Example:
# Want summary → num_predict=100
# Want full blog → num_predict=800
