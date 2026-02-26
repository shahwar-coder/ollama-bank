import ollama

response = ollama.generate(
    model='llama3',
    prompt='Explain AI agents with example',
    options={
        # creativity control
        'temperature': 0.7,
        'top_p': 0.9,

        # length control
        'num_predict': 300,

        # memory control
        'num_ctx': 8192,

        # repetition control
        'repeat_penalty': 1.2,
    }
)

print(response['response'])

'''
Q1. Why do we pass an "options" dictionary in ollama.generate()?

A.
Because options allow us to control how the model generates text.
They adjust creativity, length, randomness, and behavior.
'''
# Example:
# options={'temperature': 0.7}
# Makes output moderately creative



'''
Q2. What does "temperature" control?

A.
Temperature controls randomness.
Lower value → more predictable.
Higher value → more creative and diverse.
'''
# Example:
# temperature=0.1 → Safe, factual answer
# temperature=1.0 → Creative story



'''
Q3. What does "num_predict" mean?

A.
It controls the maximum number of tokens the model can generate.
It limits output length.
'''
# Example:
# num_predict=50 → Short answer
# num_predict=500 → Long explanation



'''
Q4. What does "top_p" control?

A.
Top_p controls nucleus sampling.
It limits token selection to the most probable tokens
within a cumulative probability range.
'''
# Example:
# top_p=0.5 → More focused output
# top_p=0.9 → More variety in wording



'''
Q5. What does "num_ctx" control?

A.
It sets the context window size for that request.
It defines how many tokens the model can process.
'''
# Example:
# num_ctx=4096 → Smaller memory
# num_ctx=16384 → Larger memory (if model supports it)



'''
Q6. What does "repeat_penalty" do?

A.
It reduces repetition by penalizing tokens
that were already used frequently.
'''
# Example:
# repeat_penalty=1.0 → Normal
# repeat_penalty=1.5 → Less repetitive output



'''
Q7. What is the core mental model of generation parameters?

A.
They control:
- Creativity (temperature)
- Length (num_predict)
- Diversity (top_p)
- Memory size (num_ctx)
- Repetition control (repeat_penalty)
'''
# Example:
# Story writing → Higher temperature
# Technical answer → Lower temperature