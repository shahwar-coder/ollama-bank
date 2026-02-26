'''
Q1. What does temperature control in text generation?

A.
Temperature controls randomness and creativity in the model's output.
Lower values make the output more predictable.
Higher values make it more creative.
'''
# Example:
# temperature=0.1 → Very factual explanation
# temperature=1.0 → More imaginative wording



'''
Q2. What happens when temperature is set to 0.0?

A.
The model becomes almost deterministic.
It tends to pick the most probable next token every time.
'''
# Example:
# Ask twice with temperature=0.0
# Output will likely be identical



'''
Q3. What is a good temperature for factual answers?

A.
Around 0.2 to 0.4.
This keeps responses safe and reliable.
'''
# Example:
# temperature=0.3
# Output: Clear, structured, less creative



'''
Q4. What is a good temperature for storytelling?

A.
Around 0.7 to 1.0.
This balances structure with creativity.
'''
# Example:
# temperature=0.8
# Output: More expressive and imaginative story



'''
Q5. What happens if temperature goes above 1.2?

A.
The output may become chaotic.
It may include unexpected or less coherent responses.
'''
# Example:
# temperature=1.5
# Story may jump topics or become unpredictable



'''
Q6. What is the simple mental model for temperature?

A.
Temperature = risk-taking level.
Low risk → safe answers.
High risk → creative answers.
'''
# Example:
# Risk level 0.2 → Conservative explanation
# Risk level 1.0 → Bold and creative wording
