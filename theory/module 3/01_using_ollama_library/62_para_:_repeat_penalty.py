'''
Q1. What does repeat_penalty control?

A.
repeat_penalty reduces the probability of tokens
that the model has already used.
It helps prevent repetitive output.
'''
# Example:
# Without penalty → "AI is powerful. AI is powerful. AI is powerful."
# With penalty → More varied wording



'''
Q2. What happens when repeat_penalty = 1.0?

A.
There is no penalty.
The model can freely repeat words or phrases.
'''
# Example:
# repeat_penalty=1.0
# Output may contain repeated sentences



'''
Q3. What is a typical good range for repeat_penalty?

A.
Between 1.1 and 1.3.
It reduces repetition without harming fluency.
'''
# Example:
# repeat_penalty=1.2
# Output becomes smoother and less repetitive



'''
Q4. What happens if repeat_penalty is set very high (e.g., 1.5)?

A.
The model aggressively avoids repeating words.
This may sometimes reduce clarity.
'''
# Example:
# repeat_penalty=1.5
# Model avoids repeating key terms even when needed



'''
Q5. Why is repeat_penalty important in long generations?

A.
Because long outputs increase the risk of loops
or repeated phrases.
Penalty helps maintain diversity.
'''
# Example:
# Long story generation
# Prevents repeating the same sentence pattern



'''
Q6. What is the simple mental model for repeat_penalty?

A.
repeat_penalty = anti-loop control.
Higher value → stronger repetition control.
'''
# Example:
# 1.0 → No anti-loop
# 1.2 → Balanced anti-loop
# 1.5 → Strong anti-loop
