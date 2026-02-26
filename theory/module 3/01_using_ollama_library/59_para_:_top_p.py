'''
Q1. What does top_p control in text generation?

A.
top_p controls how many possible next tokens the model considers.
It selects the smallest group of tokens whose total probability
is greater than or equal to the top_p value.
'''
# Example:
# top_p=0.3 → Only highest-probability words considered
# top_p=0.9 → Much larger pool of candidate words



'''
Q2. How is top_p different from temperature?

A.
Temperature adjusts randomness across all tokens.
top_p limits the candidate pool before sampling.
'''
# Example:
# temperature → changes risk level
# top_p → changes how wide the word selection pool is



'''
Q3. What happens when top_p is set to 0.3?

A.
The model becomes very focused.
It only considers a small set of highly probable tokens.
'''
# Example:
# top_p=0.3
# Output → More precise and conservative



'''
Q4. What happens when top_p is set to 1.0?

A.
The model considers the full probability distribution.
All possible tokens can be sampled.
'''
# Example:
# top_p=1.0
# Output → Maximum diversity possible



'''
Q5. What is a balanced top_p value?

A.
Around 0.7 to 0.9.
It allows diversity while keeping responses coherent.
'''
# Example:
# top_p=0.8
# Output → Natural, varied, but still structured



'''
Q6. What is the simple mental model for top_p?

A.
top_p = how wide the candidate pool is.
Smaller value → narrow pool.
Larger value → wider pool.
'''
# Example:
# Pool width 0.3 → Few safe options
# Pool width 0.9 → Many possible options
