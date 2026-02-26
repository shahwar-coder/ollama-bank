'''
🔎 Keyword Search vs Semantic Search (RAG Perspective)

----------------------------------------------------
1️⃣ Keyword Search (Lexical Search)
----------------------------------------------------
👉 Idea:
Match exact words between query and documents

👉 How it works:
- Uses techniques like TF-IDF / BM25
- Counts word frequency and overlap
- Ranking based on keyword relevance

👉 Example:
Query: "python list reverse"

Returns docs containing:
- "python"
- "list"
- "reverse"

👉 Pros:
✓ Fast
✓ Simple
✓ Works well for exact queries

👉 Cons:
✗ Cannot understand meaning
✗ Misses synonyms ("invert" vs "reverse")
✗ Poor for natural language questions

👉 In RAG:
Used as baseline retriever but limited reasoning support


----------------------------------------------------
2️⃣ Semantic Search (Vector Search)
----------------------------------------------------
👉 Idea:
Match meaning instead of exact words

👉 How it works:
- Convert text → embeddings
- Store embeddings in vector DB
- Retrieve using similarity (cosine, dot, L2)

👉 Example:
Query: "How to invert a list in python?"

Can retrieve doc:
"reverse a python list"

👉 Pros:
✓ Understands intent
✓ Handles paraphrases
✓ Better recall for natural questions

👉 Cons:
✗ Requires embedding model
✗ Approximate retrieval
✗ Infra complexity


----------------------------------------------------
🎯 Key Difference
----------------------------------------------------
Keyword → word overlap
Semantic → meaning similarity


----------------------------------------------------
🚀 In Modern RAG Systems
----------------------------------------------------
Best practice = Hybrid Retrieval

👉 Keyword search → precision
👉 Semantic search → recall

Together:
Higher retrieval quality → better generation
'''