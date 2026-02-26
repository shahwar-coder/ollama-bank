'''
🧠 Step 5 — Generation (LLM) in RAG

Flow:
[Query + Retrieved chunks] → LLM → Answer

👉 Final prompt structure:
- Context: retrieved relevant chunks
- Question: user query

👉 LLM behavior:
- Uses provided context as knowledge source
- Generates answer conditioned on retrieved data

👉 Benefit:
Grounded generation → reduces hallucinations

⭐ Summary:
Retrieved context + query → LLM → context-aware answer
'''

# =================

'''
Q1. What happens in Step 5 — Generation?

A.
After retrieval, the system sends two things to the LLM:
1. The user question
2. The retrieved chunks (context)

The LLM generates an answer using that context.
'''
# Example:
# Context: "Photosynthesis converts sunlight into energy..."
# Question: "How does photosynthesis work?"
# LLM → grounded explanation



'''
Q2. Why do we include retrieved chunks in the prompt?

A.
Because the LLM needs reliable knowledge
to answer accurately.
Without context, it may guess.
With context, it stays grounded.
'''
# Example:
# No context → generic answer
# With context → specific, accurate answer



'''
Q3. What does “grounded generation” mean?

A.
It means the LLM bases its answer
on provided external knowledge
instead of only its internal memory.
'''
# Example:
# Internal guess → possible hallucination
# External chunk provided → factual response



'''
Q4. How does RAG reduce hallucinations?

A.
By supplying real documents as context,
the LLM relies less on guessing
and more on actual retrieved information.
'''
# Example:
# Retrieved company policy
# LLM answers according to policy text



'''
Q5. What does the final prompt look like conceptually?

A.
It combines:
- Retrieved context
- User question

So the LLM sees both together.
'''
# Example:
# "Based on the following context:
# [retrieved text]
# Answer the question:
# [user question]"



'''
Q6. What happens if retrieval is poor in this step?

A.
If wrong chunks are retrieved,
the LLM will generate an incorrect answer,
even if it sounds confident.
'''
# Example:
# Wrong medical document retrieved
# → Incorrect medical explanation



'''
Q7. Why is generation dependent on retrieval quality?

A.
Because RAG is:
Retrieval → Generation.
Generation can only use what retrieval provides.
'''
# Example:
# Good retrieval → strong answer
# Bad retrieval → weak or wrong answer



'''
Q8. Strong mental model of Step 5:

A.
Think of the LLM as a smart writer.
Retrieval gives it research notes.
The LLM writes the final answer using those notes.
'''
# Example:
# Research notes = retrieved chunks
# Final essay = generated response



'''
Q9. Interview-ready explanation of the generation step:

A.
In the final stage of RAG,
the LLM receives both the user query
and the retrieved document chunks.
It generates a response grounded in that context,
reducing hallucination and improving factual accuracy.
'''
# Example:
# Query + top-k chunks → grounded answer
