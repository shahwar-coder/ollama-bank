'''
Quantization – Three Core Benefits
==================================

1) Reduced Memory Usage
-----------------------
Quantization reduces the number of bits used per parameter.

Example:
    FP32  -> 32 bits per parameter
    INT8  -> 8 bits per parameter
    Q4    -> 4 bits per parameter

Result:
    - Model size becomes 2x to 8x smaller
    - Fits into smaller RAM / VRAM
    - Enables running large models on laptops


2) Faster Inference
-------------------
Lower precision means lighter computation.

Smaller numbers:
    - Move faster through memory
    - Use less memory bandwidth
    - Require fewer CPU/GPU operations

Result:
    - Faster token generation
    - Lower latency
    - More efficient local inference


3) Lower Hardware Requirements
-------------------------------
Because models are smaller and lighter:

    - Can run on CPU-only machines
    - Can run on consumer GPUs
    - Can run on edge devices

Result:
    - Local AI becomes practical
    - Deployment cost is reduced
    - On-device AI becomes feasible


Summary
-------
Quantization = Smaller model + Faster inference + Lower hardware cost
'''