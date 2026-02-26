'''
Q1. Why does generating 311 tokens take noticeable time?

A.
Because LLMs generate tokens sequentially.
For 311 tokens, the model runs 311 forward passes.
Each token requires a full computation step.
'''
# Example:
# 5 tokens/sec → 311 tokens ≈ 62 seconds
# 10 tokens/sec → 311 tokens ≈ 31 seconds



'''
Q2. Why is an 8B model slower than a 1B model?

A.
An 8B model has about 8× more parameters than a 1B model.
More parameters mean more computation per token.
'''
# Example:
# 1B → smaller matrix multiplications
# 8B → much larger matrix multiplications
# Result → slower per-token speed



'''
Q3. What is the main hidden bottleneck during inference?

A.
Memory bandwidth.
The system must repeatedly load model weights from memory.
Moving large weights is often slower than the math itself.
'''
# Example:
# 8B weights → several GB moved repeatedly
# Limited RAM bandwidth → slower generation



'''
Q4. How does 8GB RAM affect performance?

A.
Large models consume significant memory.
This creates memory pressure, cache misses, or even swapping.
That slows down token generation.
'''
# Example:
# 8B quantized model uses multiple GB
# Less free memory → slower access



'''
Q5. Why is CPU inference slower than GPU inference?

A.
CPUs have fewer cores and lower memory bandwidth.
GPUs are optimized for large matrix multiplications.
Transformers rely heavily on matrix operations.
'''
# Example:
# CPU → few parallel units
# GPU → thousands of parallel cores
# GPU → much faster token throughput



'''
Q6. Why does output length increase total latency?

A.
Because total generation time equals:
tokens × time_per_token.
More tokens mean more sequential computation steps.
'''
# Example:
# 3 tokens/sec
# 300 tokens → 100 seconds



'''
Q7. Why is a 1B model noticeably faster?

A.
It has fewer parameters,
smaller memory footprint,
better cache locality,
and less memory movement.
'''
# Example:
# 1B → fits better in memory
# 8B → heavier memory load
# Result → 1B higher tokens/sec



'''
Q8. What is the role of KV cache in slowdown?

A.
During generation, attention states are stored in KV cache.
As tokens increase, the cache grows.
Larger models create larger cache structures.
'''
# Example:
# 311 tokens → 311 attention states stored
# Bigger model → larger cache size



'''
Q9. What are the three main knobs controlling latency?

A.
1. Model size
2. Output length (num_predict)
3. Hardware capability
'''
# Example:
# Smaller model + shorter output + GPU
# → fastest configuration



'''
Q10. What is the ultra-simple performance formula?

A.
Latency ≈ model_size × tokens / hardware_power.
'''
# Example:
# Large model + many tokens + weak CPU
# → slow generation
