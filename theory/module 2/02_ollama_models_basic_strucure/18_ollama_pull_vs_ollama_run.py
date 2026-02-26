'''
Difference Between `ollama pull` and `ollama run`
==================================================

1. ollama pull <model>

Purpose:
    Downloads the model from Ollama's remote repository
    to your local system.

What it does:
    - Connects to Ollama registry
    - Downloads the GGUF model file
    - Verifies file integrity (hash check)
    - Stores it locally on your machine

Important:
    It DOES NOT run the model.
    It only ensures the model exists locally.

Think of it as:
    "Install the model"

------------------------------------------------------------

2. ollama run <model>

Purpose:
    Loads and runs the model for inference.

What it does:
    Step 1: Checks if model exists locally
    Step 2: If NOT found → automatically performs pull
    Step 3: Loads model weights into RAM (or GPU if available)
    Step 4: Starts inference session (chat mode)
    Step 5: Waits for your prompt

Think of it as:
    "Start using the model"

------------------------------------------------------------

How `run` Manages Missing Models
================================

When you type:

    ollama run qwen

Ollama internally performs:

    IF model exists locally:
        Load into memory and start
    ELSE:
        Download model (pull)
        Store locally
        Then load into memory

So:
    `run` automatically triggers `pull`
    if the model is not already downloaded.

------------------------------------------------------------

Where the Model Is Stored
=========================

On macOS:
    ~/.ollama/models/

The downloaded GGUF file stays there permanently
until you remove it using:

    ollama rm <model>

------------------------------------------------------------

What Happens During Run (Memory Flow)
=====================================

Disk (GGUF file)
        ↓
Loaded into RAM (and optionally GPU)
        ↓
Inference engine starts
        ↓
You interact via terminal or API

When you exit:
    - Model is unloaded from RAM
    - File remains on disk

------------------------------------------------------------

Simple Summary
==============

pull  → Download model to disk
run   → Load model into memory and use it

If model not present:
    run automatically performs pull first.

------------------------------------------------------------

Golden Mental Model

pull = install
run  = execute
rm   = uninstall
'''