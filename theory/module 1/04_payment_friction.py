'''
Why LLM Providers Ask for Payment

In cloud-based LLM systems:

User → API Call → Cloud LLM → Response

Why Payment is Required:

1. Infrastructure Cost
   - Powerful GPUs are expensive.
   - Servers run 24/7.
   - Cooling, electricity, maintenance cost money.

2. Per-Token Pricing Model
   - You pay based on how many tokens you use.
   - More usage = More cost.
   - Large prompts + long responses increase price.

3. Research & Model Training Cost
   - Training large models costs millions of dollars.
   - Companies recover that cost via API pricing.

How It Works:

- You sign up.
- Add billing details.
- Every API request deducts cost from your balance.

Contrast with Local LLM (e.g., Ollama):

- You download the model once.
- Runs on your own hardware.
- No per-token API charges.
- Only cost = your hardware + electricity.

Simple Mental Model:

Cloud LLM = Renting a supercomputer (pay per use).
Local LLM = Buying your own machine (one-time cost).
'''
