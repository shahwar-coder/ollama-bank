'''
👉 "Keyword search relies on lexical overlap" — meaning

🔎 Lexical overlap =
Number of common words between query and document

Keyword search works by:
- Breaking text into words (tokens)
- Counting how many words match
- Ranking documents with more matching words higher

-----------------------------------
Example
-----------------------------------

Query:
"python list reverse"

Doc A:
"python list reverse method"
→ Overlap = python, list, reverse (3 matches) ✅

Doc B:
"how to invert a list in python"
→ Overlap = list, python (2 matches)
→ "invert" ≠ "reverse" → not counted ❌

👉 So Doc A ranks higher

-----------------------------------
Key insight
-----------------------------------
Keyword search cares about:
✓ Exact words
✓ Word frequency
✓ Word positions

But NOT:
✗ Meaning
✗ Synonyms
✗ Intent

👉 That is why semantic search exists
'''