'''
Ollama Can Be Accessed in Multiple Ways

Ollama is not just a terminal tool.
It exposes multiple interfaces.

1. CLI (Command Line Interface)

   ollama run llama3
   ollama pull mistral

- Easiest way to interact.
- Direct chat in terminal.
- Good for testing and quick usage.


2. REST API (localhost)

When Ollama runs, it starts a local server:

   http://localhost:11434

You can send HTTP requests to:

   POST /api/generate
   POST /api/chat
   POST /api/embeddings

This allows:
- Backend integration
- Web apps
- Mobile apps
- Agent systems


3. Python SDK

You can use Ollama directly in Python:

   from ollama import chat

- Cleaner integration.
- Used in FastAPI apps.
- Used in RAG pipelines.
- Used in AI agents.


---------------------------------------
How They Connect

Ollama Core Engine
        ↓
Exposes:
   CLI
   REST API
   Python Interface

All of them talk to the SAME local model.

---------------------------------------
Mental Model

Ollama = Engine
CLI = Manual control
REST API = Web access
Python SDK = Developer integration

Same brain.
Different access methods.
'''
