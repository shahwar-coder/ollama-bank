'''
Q1. What is an OCI image?
A.
An OCI (Open Container Initiative) image is a standardized format
for packaging container images. It consists of filesystem layers
and metadata so different runtimes (Docker, Podman, containerd)
can understand and run the same image.
'''

# Example structure:
# Image
# ├── Manifest
# ├── Config
# └── Layers


'''
Q2. What does “layered image system” mean?
A.
It means a container image is built as a stack of filesystem layers,
where each layer contains only the changes from the previous one.
The final filesystem is created by merging these layers.
'''

# Example:
# Layer1 → base OS
# Layer2 → install Python
# Layer3 → copy app
# Final FS = L1 + L2 + L3


'''
Q3. Why are layers powerful?
A.
Layers allow reuse, caching, and incremental downloads.
If multiple images share the same base layer,
it is downloaded only once.
'''

# Example:
# ubuntu:22.04 used in 10 images
# Base layer pulled once → reused everywhere


'''
Q4. What are the three main components inside an OCI image?
A.
1) Manifest → table of contents listing layers and config
2) Config → runtime metadata (entrypoint, env, etc.)
3) Layers → compressed filesystem diffs stored as blobs
'''

# Example:
# Manifest → references sha256 hashes
# Config → defines CMD and ENV
# Layers → contain /usr/bin, /app, etc.


'''
Q5. What does “content-addressed” mean in OCI?
A.
Each layer is identified by a cryptographic hash (e.g., sha256).
The hash uniquely represents the content,
ensuring integrity and enabling deduplication.
'''

# Example:
# sha256:abc123 → exact layer content
# If content changes → hash changes


'''
Q6. What happens when you run `docker pull`?
A.
1) Client fetches manifest
2) Checks which layer hashes exist locally
3) Downloads missing blobs
4) Verifies hashes
5) Assembles layered filesystem
'''

# Example workflow:
# Pull manifest → download only missing layers → mount union FS


'''
Q7. Why is OCI important beyond Docker?
A.
OCI became a universal artifact distribution standard.
It is used for container images, WASM modules,
Helm charts, and even LLM model packaging (e.g., Ollama).
'''

# Example:
# OCI = transport protocol for artifacts
# Like Git for filesystems