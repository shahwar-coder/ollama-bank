'''
Yes — Correct.

If you have already downloaded the model:

    ollama pull llama3.2:1b

Then later when you run:

    ollama run llama3.2:1b

What happens?

1. No re-download.
   - Model is already stored locally.
   - Located in ~/.ollama/models (mac/Linux)
     or equivalent directory on Windows.

2. Ollama loads model into RAM.
   - Reads GGUF file from disk.
   - Allocates memory.
   - Initializes runtime.

3. Inference is ready.
   - You see:
       >>> Send a message

Only first time → download.
After that → load into memory.

----------------------------------

When does it download again?

- If model was never pulled before.
- If you explicitly remove it:
      ollama rm llama3.2:1b
- If you pull a newer version.

----------------------------------

Simple Mental Model:

First time:
    Internet → Download → Store on disk

Every next time:
    Disk → Load into RAM → Run

No internet required after download.
'''
