'''
Q1. What is a context window?

A.
A context window is the maximum number of tokens a model can see and use at one time.
It includes the input and the output being generated.
'''
# Example:
# Context = 8000 tokens
# Input = 5000 tokens
# Max output possible ≈ 3000 tokens



'''
Q2. What all fits inside a context window?

A.
The context window includes:
- System prompt
- Conversation history
- Current user prompt
- Generated output (so far)
All of this must fit inside the limit.
'''
# Example:
# System = 400 tokens
# History = 2000 tokens
# User prompt = 600 tokens
# Total used = 3000 tokens



'''
Q3. What is the unit of measurement for context window?

A.
Context window is measured in tokens.
Not words. Not characters. Only tokens.
'''
# Example:
# "Hello world" ≈ 2 tokens
# 8k context = 8000 tokens



'''
Q4. What happens when the context limit is exceeded?

A.
When the limit is crossed, older tokens are removed.
The model can no longer see that information.
'''
# Example:
# Context limit = 4096
# If conversation grows beyond 4096 tokens
# Old messages are dropped



'''
Q5. Why is context window important?

A.
It determines how much information the model can reason over at once.
Larger context allows longer conversations and bigger documents.
'''
# Example:
# 4k context → small chats
# 32k context → large documents or long discussions



'''
Q6. Is context window the same as memory?

A.
No.
Context window is working memory (temporary).
It does not store information permanently.
'''
# Example:
# Like RAM in a computer
# When chat ends, memory is gone



'''
Q7. Why can't we increase context window infinitely?

A.
Because transformer attention requires more compute and memory as tokens increase.
More tokens mean heavier processing.
'''
# Example:
# Attention complexity = O(n²)
# 1000 tokens → manageable
# 10000 tokens → much more compute required



'''
Q8. What does 8k or 32k context mean?

A.
It means the model can process 8000 or 32000 tokens at one time.
Input + output together must stay within that number.
'''
# Example:
# 32k model
# Input = 20k tokens
# Output max ≈ 12k tokens