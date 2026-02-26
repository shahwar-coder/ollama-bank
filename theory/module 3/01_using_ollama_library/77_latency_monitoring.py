'''
Q1. What is latency?

A.
Latency is the time taken by a system to respond
to a request.
It is measured as response_time - request_time.
'''
# Example:
# User sends request at 10:00:00
# Response received at 10:00:03
# Latency = 3 seconds



'''
Q2. What is latency monitoring?

A.
Latency monitoring means continuously measuring
how long a system takes to respond.
It helps detect slowdowns or instability.
'''
# Example:
# API response times tracked every minute
# Alert triggered if latency > 2 seconds



'''
Q3. Why is latency monitoring important?

A.
Because performance can degrade over time.
Monitoring helps detect regressions early.
'''
# Example:
# Yesterday p95 = 800ms
# Today p95 = 2.5s
# Something is wrong



'''
Q4. What is TTFT in LLM systems?

A.
TTFT (Time To First Token) measures
how long it takes for the model
to generate the first token after receiving a prompt.
'''
# Example:
# Prompt sent at 0.0s
# First token at 1.2s
# TTFT = 1.2 seconds



'''
Q5. What is token latency?

A.
Token latency measures how fast tokens
are generated after the first token.
It reflects decoding speed.
'''
# Example:
# 20 tokens/sec
# Faster hardware → higher tokens/sec



'''
Q6. What is full response latency?

A.
It is the total time from prompt
to final generated answer.
It reflects user experience.
'''
# Example:
# TTFT = 1s
# Generation time = 5s
# Full latency = 6s



'''
Q7. Why are p50, p95, and p99 important?

A.
Because averages can hide slow cases.
Tail latency (p95, p99) shows worst-user experience.
'''
# Example:
# Avg = 1s
# p95 = 5s
# → Some users experience big delays



'''
Q8. Where is latency monitoring used?

A.
It is used in APIs, databases, LLM systems,
mobile apps, and any interactive service.
'''
# Example:
# API request time
# Database query time
# LLM generation time



'''
Q9. What is the mental model for latency monitoring?

A.
Latency monitoring = performance health check.
It ensures the system remains responsive.
'''
# Example:
# Like checking heart rate
# If abnormal → investigate



'''
Q10. What is the AI engineer definition of latency monitoring?

A.
Latency monitoring is the continuous measurement
and analysis of response times across system components
to ensure performance, detect degradation,
and maintain service-level objectives.
'''
# Example:
# Monitor TTFT, tokens/sec, p95 latency
# Maintain SLA under 3 seconds