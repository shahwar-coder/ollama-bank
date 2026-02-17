'''
1. Weights and Biases → What are they in an LLM?

- An LLM is a huge neural network.
- Inside it, there are millions/billions of numbers.
- These numbers are called "weights" and "biases".

Think of them as:
- Weights → Strength of connections between neurons.
- Biases → Adjustment values that fine-tune decisions.

Together, weights + biases store the model’s knowledge.

Example:
If the model knows that:
"Paris is the capital of France"

That knowledge is NOT stored as a sentence.
It is stored inside these numerical weights.


2. This is the learning an LLM has

During training:
- The model reads massive amounts of text.
- It predicts next words.
- It adjusts weights and biases.
- It repeats this billions of times.

This adjustment process = learning.

So:
Learning = updating weights and biases based on data.

After training:
The model no longer "learns".
It just uses fixed weights to generate outputs.


3. This is hosted in cloud…

In cloud-based AI systems:
- The trained model (weights + biases)
- Is stored on company servers (OpenAI, etc.)
- You access it via API.

You DO NOT:
- See the weights
- Download the full model
- Control training

With local systems (like Ollama):
- You download the model weights to your machine.
- They run locally.
- No cloud dependency required.

Simple Mental Model:

LLM = Brain
Weights & Biases = Memory inside the brain
Training = Learning process
Cloud hosting = Brain lives on someone else's computer
Local hosting = Brain lives on your computer
'''
