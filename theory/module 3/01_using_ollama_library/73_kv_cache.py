'''
Q1. What problem does the KV cache solve?

A.
Without KV cache, the model would recompute attention
for all previous tokens at every new generation step.
KV cache stores past attention values to avoid recomputation.
'''
# Example:
# Token4 attends to token1,2,3
# With cache → reuse stored data
# Without cache → recompute all from scratch



'''
Q2. What does "KV" stand for?

A.
K = Key
V = Value
They are tensors produced during transformer attention.
They represent stored information from previous tokens.
'''
# Example:
# Token1 → produces K1, V1
# Token2 → produces K2, V2



'''
Q3. How does generation work step-by-step with KV cache?

A.
For each new token:
1. Compute its Query (Q)
2. Use stored K and V from previous tokens
3. Compute attention
4. Store new K and V in cache
'''
# Example:
# Step1 → store K1,V1
# Step2 → use K1,V1 then store K2,V2
# Step3 → use K1,V1,K2,V2



'''
Q4. Why is KV cache critical for fast inference?

A.
Because it avoids recomputing attention for past tokens.
Only the new token requires fresh computation.
'''
# Example:
# Chat without cache → extremely slow
# Chat with cache → practical speed



'''
Q5. What is the cost of KV cache?

A.
It consumes memory.
The cache grows as more tokens are generated.
'''
# Example:
# 50 tokens → small cache
# 300 tokens → much larger cache



'''
Q6. How is KV cache related to context window?

A.
Context window defines maximum tokens allowed.
KV cache stores the attention data for those tokens.
'''
# Example:
# num_ctx=8192 → up to 8192 tokens
# KV cache stores K,V for each of them



'''
Q7. Why do larger models have larger KV caches?

A.
Because larger models have:
- More layers
- Larger hidden dimensions
Each token stores more data per layer.
'''
# Example:
# 1B model → smaller hidden size
# 8B model → bigger hidden size → larger KV memory



'''
Q8. Why did generating 311 tokens slow down on CPU?

A.
Because 311 tokens created a growing KV cache.
On limited memory bandwidth hardware,
moving that memory repeatedly slows generation.
'''
# Example:
# 311 tokens × many layers
# → Increased memory movement → slower speed



'''
Q9. What is the ultra-simple mental model of KV cache?

A.
Weights = long-term knowledge
KV cache = short-term conversation memory
'''
# Example:
# Weights → model training knowledge
# KV cache → current chat memory



'''
Q10. What is the interview-level definition of KV cache?

A.
KV cache is an inference optimization that stores previously
computed key and value tensors from transformer attention layers,
allowing future token generation to reuse past computations
instead of recomputing them.
'''
# Example:
# Store K1,V1 once
# Reuse them for token2, token3, token4
