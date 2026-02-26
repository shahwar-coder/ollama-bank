'''
Q1. What does num_ctx control?

A.
num_ctx controls the context window size.
It defines how many tokens the model can see in one request.
'''
# Example:
# num_ctx=8192
# Model can process up to 8192 tokens total



'''
Q2. What tokens are included inside num_ctx?

A.
It includes:
- System prompt
- Conversation history
- Current user prompt
- Generated output
All together must fit within num_ctx.
'''
# Example:
# Prompt = 2000 tokens
# History = 3000 tokens
# Output = 1000 tokens
# Total = 6000 tokens (must be ≤ num_ctx)



'''
Q3. What happens if total tokens exceed num_ctx?

A.
Older tokens may be truncated.
The model will lose access to that information.
'''
# Example:
# num_ctx=4096
# If conversation grows to 5000 tokens
# First 904 tokens may be dropped



'''
Q4. Can we increase num_ctx infinitely?

A.
No.
You cannot exceed the model’s architecture limit.
It is defined during training.
'''
# Example:
# Model trained with 8k context
# Cannot safely run at 128k



'''
Q5. What is the simple mental model for num_ctx?

A.
num_ctx = model’s working memory size (RAM).
'''
# Example:
# Small RAM → short conversations
# Large RAM → long conversations and big documents
