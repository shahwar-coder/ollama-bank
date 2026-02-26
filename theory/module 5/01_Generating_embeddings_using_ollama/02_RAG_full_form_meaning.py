'''
Q1. What does "Retrieval" mean in Retrieval Augmented Generation?

A.
Retrieval means fetching relevant information
from an external knowledge source before generating an answer.
'''
# Example:
# User asks: "Company leave policy?"
# System retrieves policy document from database



'''
Q2. What does "Augmented" mean in Retrieval Augmented Generation?

A.
Augmented means enhanced or improved.
The retrieved information is added to the prompt
to improve the model’s answer.
'''
# Example:
# Question + Retrieved document
# → Combined prompt sent to LLM



'''
Q3. What does "Generation" mean in Retrieval Augmented Generation?

A.
Generation means the LLM produces a final answer
using both the user query and retrieved context.
'''
# Example:
# LLM reads retrieved text
# Generates grounded answer



'''
Q4. Why is it called Retrieval Augmented Generation?

A.
Because the process has three clear steps:
1. Retrieve relevant data
2. Augment the prompt with that data
3. Generate the final response
'''
# Example:
# Search document → Add to prompt → Produce answer



'''
Q5. What happens if we remove Retrieval from RAG?

A.
The model answers using only its internal training knowledge.
This increases hallucination risk.
'''
# Example:
# No retrieval → Model guesses
# With retrieval → Model references actual data



'''
Q6. What is the full mental model of RAG in one line?

A.
Retrieve knowledge,
Augment the prompt,
Generate the answer.
'''
# Example:
# Open-book exam:
# Look up info → Use it → Write answer
