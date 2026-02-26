'''
Ollama Pull – What Is the Manifest File?
=========================================

When you run:

    ollama pull <model>

Ollama first downloads a MANIFEST file.

The manifest is a JSON file that describes
everything required to reconstruct and run the model locally.

It does NOT contain the model weights directly.
It contains references (IDs) to the required components.

Think of it as:
    A blueprint + resource map for the model.

------------------------------------------------------------
What Are the IDs in the Manifest?
------------------------------------------------------------

The long values like:

    sha256:8c17c2ebb0ea...

are content hashes.

These are:

    - Unique fingerprints of each file
    - Used for integrity verification
    - Used to identify each component uniquely

If even one byte changes,
the hash changes.

So:

    ID = cryptographic fingerprint of a file

------------------------------------------------------------
Manifest Structure (High-Level)
------------------------------------------------------------

The manifest JSON usually contains:

    - header
    - config
    - layers

Each has a specific purpose.

------------------------------------------------------------
1. Header
------------------------------------------------------------

Contains general metadata about the model image.

Examples:
    schemaVersion
    mediaType

Purpose:
    - Defines format version
    - Defines how the file should be interpreted
    - Ensures compatibility

Think of it as:
    "File format declaration"

------------------------------------------------------------
2. Config
------------------------------------------------------------

Points to a configuration blob.

Example fields:
    mediaType: application/vnd.ollama.image.config
    digest: sha256:...
    size: ...

This config file contains:
    - Model architecture info
    - Parameters
    - Template info
    - Default runtime settings
    - Tokenizer info

This is NOT the weights.
This is metadata about how to run the model.

Think of it as:
    "How to use the model"

------------------------------------------------------------
3. Layers
------------------------------------------------------------

Layers are the actual data blobs required to run the model.

Each layer entry includes:
    - mediaType
    - digest (sha256 hash)
    - size

Common layer types:
    - model weights (GGUF)
    - license
    - template
    - parameters

The largest layer is typically:
    The GGUF weights file (several GB)

Smaller layers:
    - License text
    - Prompt template
    - JSON parameter defaults

Think of layers as:
    The actual downloadable pieces of the model

------------------------------------------------------------
What Happens During Pull?
------------------------------------------------------------

Step 1:
    Download manifest JSON

Step 2:
    Read manifest → identify required layers

Step 3:
    Download each layer by its SHA256 ID

Step 4:
    Verify SHA256 hash of each layer

Step 5:
    Store layers locally

Step 6:
    Write local manifest entry

Now model is ready to run.

------------------------------------------------------------
Why This Design?
------------------------------------------------------------

Because Ollama follows an OCI-style image format,
similar to Docker images.

Benefits:
    - Deduplication (shared layers)
    - Integrity verification
    - Modular design
    - Efficient caching

------------------------------------------------------------
Simple Mental Model
------------------------------------------------------------

Manifest = Table of contents
Config   = Model settings & metadata
Layers   = Actual downloadable files
IDs      = Fingerprints ensuring correctness

------------------------------------------------------------
Very Important Insight
------------------------------------------------------------

The manifest does not contain the model.
It contains references to everything needed
to reconstruct the model locally.

That is why "pulling manifest" appears first
before large file downloads begin.
'''