'''
LLM Speed & Efficiency – Quick Revision

Why are local LLMs (GGUF-based) fast?

Two main reasons:

1️⃣ Quantization
   - Converts high-precision weights (float32/16)
     into lower-bit versions (Q4, Q5, Q8).
   - Reduces model size.
   - Lowers RAM usage.
   - Speeds up matrix computations.
   - Small accuracy trade-off, big speed gain.

2️⃣ Memory Mapping (mmap)
   - Model stays on disk.
   - Only required parts are loaded into RAM.
   - No full model copy needed.
   - Faster startup.
   - More efficient memory usage.

Supporting Concepts:

- Blueprint → Model architecture (structure).
- Weights → Learned knowledge (billions of numbers).
- Indices → Help locate tensors efficiently.

Final Summary:

Speed = Quantized Weights + Efficient Memory Access

GGUF works fast because it:
✓ Compresses weights (quantization)
✓ Loads efficiently (memory mapping)
✓ Minimizes RAM & compute overhead
'''
