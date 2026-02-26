'''
Q1. What is chunking in RAG?

A.
Chunking is the process of splitting large documents
into smaller, meaningful pieces before embedding.
'''
# Example:
# 50-page PDF
# → Split into paragraphs
# → Each paragraph becomes a chunk



'''
Q2. Why can’t we embed entire documents directly?

A.
Because large documents exceed embedding limits
and reduce retrieval precision.
Smaller chunks produce better semantic matching.
'''
# Example:
# 10,000-token document
# → Hard to match specific question
# 300-token chunk
# → Much more precise retrieval



'''
Q3. Why does chunking improve retrieval quality?

A.
Because retrieval works at chunk level.
Smaller chunks mean more relevant matches
and less unrelated context.
'''
# Example:
# User asks about refund deadline
# System retrieves only refund section
# Not the entire policy document



'''
Q4. What is a typical chunk size?

A.
Usually between 200–500 tokens.
This balances context richness and precision.
'''
# Example:
# 300-token chunk
# Enough detail
# Not too large



'''
Q5. What happens if chunks are too large?

A.
Retrieval becomes less precise.
More irrelevant information is returned.
'''
# Example:
# 2000-token chunk
# Contains refund + shipping + warranty
# User only asked about refund



'''
Q6. What happens if chunks are too small?

A.
Important context may be lost.
The answer may become incomplete.
'''
# Example:
# 20-token chunk
# Lacks surrounding explanation



'''
Q7. What is the mental model of chunking?

A.
Break big knowledge into searchable pieces.
'''
# Example:
# Book → Chapters → Pages
# Instead of searching whole book at once
