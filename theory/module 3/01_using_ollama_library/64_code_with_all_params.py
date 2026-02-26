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