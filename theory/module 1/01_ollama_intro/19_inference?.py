'''
What Does "Inference" Mean in AI?

Very Simple Definition:

Inference = Using a trained model to generate an output.

That’s it.


Two Important Phases in LLM Life:

1. Training
   - Model learns from massive data.
   - Weights & biases are adjusted.
   - Happens once (very expensive).
   - Done by big companies.

2. Inference
   - Model answers your question.
   - No learning happens.
   - Just uses existing knowledge.
   - Happens every time you type a prompt.


Example:

You type:
    "Who is the PM of India?"

Model:
    Uses trained weights
    Calculates probabilities
    Predicts next words
    Generates response

That process = Inference.


In Ollama Context:

When you run:

    ollama run llama3

And ask a question —

The model:
- Loads into memory
- Processes your prompt
- Generates tokens
- Returns output

That entire runtime process = Inference.


Simple Analogy:

Training = Studying for years.
Inference = Answering exam questions.

LLM does NOT study during inference.
It only answers using what it already learned.


One-Line Engineering Definition:

Inference = Forward pass of a trained model to produce predictions.
'''
