'''
Ollama Storage Structure – What Is Stored Where
===============================================

Default Base Directory
----------------------
Mac / Linux:
    ~/.ollama/

Windows:
    C:\Users\<username>\.ollama\

Inside this folder, Ollama organizes models in a structured way.

------------------------------------------------------------
High-Level Folder Structure
------------------------------------------------------------

.ollama/
│
├── models/
│   ├── manifests/
│   └── blobs/
│
└── (other runtime files)

------------------------------------------------------------
1) blobs/  → Actual File Storage
------------------------------------------------------------

Location:
    ~/.ollama/models/blobs/

What is stored here:
    - Model weight files (GGUF)  ← largest files (GBs)
    - License files
    - Prompt templates
    - Parameter configs
    - Any layer referenced by manifest

Important:
    Files are stored using SHA256 hashes as filenames.

Example:
    blobs/
        sha256:8c17c2ebb0ea...
        sha256:2e0493f67d0c...

Why?
    - Deduplication (shared layers across models)
    - Integrity verification
    - Efficient caching

Think:
    blobs = Raw building blocks


------------------------------------------------------------
2) manifests/  → Model Blueprints
------------------------------------------------------------

Location:
    ~/.ollama/models/manifests/

Structure example:
    manifests/
        registry.ollama.ai/
            library/
                llama3.1/
                    latest

What is stored here:
    - JSON manifest file
    - References to all required blobs (via SHA256 IDs)
    - Metadata about the model image

Manifest contains:
    - config reference
    - layers list
    - sha256 IDs
    - sizes
    - media types

Think:
    manifest = Assembly instructions


------------------------------------------------------------
3) What Happens During `ollama pull`
------------------------------------------------------------

Step 1:
    Download manifest

Step 2:
    Read manifest → get required layer IDs

Step 3:
    For each layer:
        - Check if blob exists locally
        - If missing → download into blobs/
        - Verify SHA256

Step 4:
    Store manifest locally

Now model is complete.


------------------------------------------------------------
4) What Happens During `ollama run`
------------------------------------------------------------

Step 1:
    Locate manifest

Step 2:
    Resolve required blobs

Step 3:
    Load GGUF model file (from blobs/) into memory

Step 4:
    Start inference

Important:
    run does NOT download unless something is missing.


------------------------------------------------------------
5) Where Is the Actual Model?
------------------------------------------------------------

The actual model weights (GGUF file) are stored inside:

    ~/.ollama/models/blobs/

It will be:
    - The largest file (several GBs)
    - Identified by its SHA256 filename
    - Referenced inside the manifest


------------------------------------------------------------
Simple Mental Model
------------------------------------------------------------

manifests/  → Blueprint
blobs/      → Actual files
GGUF file   → Real model weights
config blob → How to run the model
license     → Legal info
template    → Default prompt structure


------------------------------------------------------------
Why This Design?
------------------------------------------------------------

Ollama uses an OCI-style layered image system (like Docker).

Benefits:
    - Shared layers across models
    - No duplicate storage
    - Integrity verification
    - Modular updates
    - Efficient caching


------------------------------------------------------------
Summary
------------------------------------------------------------

manifests/ = Model blueprint (JSON metadata)
blobs/     = All actual files (weights, config, license, etc.)
run        = Loads blobs into memory
pull       = Ensures blobs exist and are verified
'''