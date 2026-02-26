'''
Q1. Which parameters mainly control creativity?

A.
temperature and top_p together control creativity.
temperature adjusts randomness.
top_p adjusts how wide the candidate word pool is.
'''
# Example:
# temperature=0.9, top_p=0.9 → Creative story
# temperature=0.2, top_p=0.5 → Safe, factual answer



'''
Q2. Which parameter controls verbosity?

A.
num_predict controls verbosity.
It sets the maximum number of tokens the model can generate.
'''
# Example:
# num_predict=50 → Short summary
# num_predict=500 → Detailed explanation



'''
Q3. Which parameter controls memory?

A.
num_ctx controls memory.
It defines how much total text the model can see.
'''
# Example:
# num_ctx=4096 → Short conversation
# num_ctx=16384 → Long conversation with history



'''
Q4. Which parameter improves fluency by reducing repetition?

A.
repeat_penalty improves fluency.
It reduces repeated words and looping phrases.
'''
# Example:
# repeat_penalty=1.0 → Repetition possible
# repeat_penalty=1.2 → Smoother output



'''
Q5. How do temperature and top_p interact?

A.
They work together.
temperature controls risk level.
top_p controls candidate pool size.
Balanced values produce natural text.
'''
# Example:
# temperature=0.7 + top_p=0.8
# Output → Creative but coherent



'''
Q6. What is the complete mental model of interaction?

A.
- temperature + top_p → creativity
- num_predict → verbosity
- num_ctx → memory
- repeat_penalty → fluency
'''
# Example:
# Want long creative story:
# temperature=0.8
# top_p=0.9
# num_predict=600
# repeat_penalty=1.2
