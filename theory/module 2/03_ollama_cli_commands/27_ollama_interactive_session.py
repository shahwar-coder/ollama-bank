'''
Ollama Interactive Session – What Is Happening
==============================================

When you run:

    ollama run llama3.2:1b

You start an interactive inference session.

The prompt:

    >>>

means:
    - The model is loaded into memory
    - A live session has started
    - You are inside a conversation loop

------------------------------------------------------------
What Happens Internally
------------------------------------------------------------

1) Model is loaded into RAM (or GPU if available)

2) Ollama starts a session process

3) Each message you type:
       - Is appended to conversation history
       - Is sent to the model as context
       - Model generates next response

4) The loop continues until you exit

------------------------------------------------------------
Is History Maintained?
------------------------------------------------------------

Yes — within that running session only.

Ollama maintains:

    conversation_history = [
        user_message_1,
        assistant_reply_1,
        user_message_2,
        assistant_reply_2,
        ...
    ]

Each new prompt includes previous conversation
within the model’s context window.

------------------------------------------------------------
Important Things to Keep in Mind
------------------------------------------------------------

1) History Lives in Memory

    - It exists only while session is active
    - If you exit, history is gone
    - Restarting `ollama run` starts fresh

2) Context Window Limit

    The model has a maximum context length.

    Example:
        131072 tokens (for some models)

    If conversation exceeds this,
    older messages are truncated.

3) Memory Usage Grows with Context

    Longer conversation:
        - More tokens
        - More RAM usage
        - Slower generation

4) No Automatic Long-Term Storage

    Ollama CLI does NOT persist chats to disk
    unless you build your own logging system.

5) Each Session Is Isolated

    Running:
        ollama run llama3.2:1b

    twice → creates two separate sessions.

------------------------------------------------------------
Mental Model
------------------------------------------------------------

ollama run → load model
>>>         → interactive loop
history     → temporary in-memory context
exit        → session destroyed

------------------------------------------------------------
Golden Rule
------------------------------------------------------------

Interactive CLI session = temporary working memory,
not permanent storage.
'''