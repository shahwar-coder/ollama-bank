'''
Chain of Thought (CoT) – Thinking Capability in Models

1️⃣ What is Chain of Thought?

Chain of Thought = Step-by-step reasoning.

Instead of giving a direct short answer,
the model shows intermediate reasoning steps.

Example:

Question:
    If a train travels 60 km/h for 2 hours,
    how far does it go?

Normal Answer:
    120 km

Chain-of-Thought Answer:
    Speed = 60 km/h
    Time = 2 hours
    Distance = speed × time
    = 60 × 2
    = 120 km


--------------------------------------------------

2️⃣ Why Chain of Thought Matters

It improves:
✓ Logical reasoning
✓ Math accuracy
✓ Multi-step problems
✓ Planning tasks
✓ Complex decision-making

It reduces:
- Random guessing
- Shallow responses


--------------------------------------------------

3️⃣ What Are "Thinking Models"?

Thinking models are optimized for:
- Structured reasoning
- Multi-step logic
- Deliberate computation

Examples in Ollama:
- deepseek-r1
- qwen (reasoning variants)
- lfm2.5-thinking

These models are trained or fine-tuned
to reason more carefully.


--------------------------------------------------

4️⃣ How It Works Internally

The model:
- Breaks problem into steps
- Predicts intermediate tokens
- Builds logical sequence
- Produces final answer

This is still inference —
but guided toward structured reasoning.


--------------------------------------------------

5️⃣ Important Note (Practical Engineering)

You don’t always want visible chain-of-thought.
Sometimes you want:

- Internal reasoning
- Clean final output

Modern models can:
- Think internally
- Output only final answer


--------------------------------------------------

6️⃣ Simple Mental Model

Normal model:
    Quick answer.

Thinking model:
    Think → Plan → Compute → Answer.

--------------------------------------------------

One-Line Summary:

Chain of Thought = Forcing or enabling
step-by-step reasoning to improve
accuracy in complex tasks.
'''
