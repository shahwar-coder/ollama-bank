'''
Q1. What is the fundamental difference between keyword search and semantic search?

A.
Keyword search matches exact words.
Semantic search matches meaning.
'''
# Example:
# Query: "invert a list"
# Doc: "reverse a list"
# Keyword → may miss
# Semantic → retrieves



'''
Q2. How does keyword search work in simple terms?

A.
It counts word overlap between the query and documents.
More matching words → higher rank.
It does not understand meaning.
'''
# Example:
# Query: "python list reverse"
# Docs containing those exact words rank higher



'''
Q3. Why is keyword search brittle in RAG?

A.
Because users ask questions in many different ways.
If wording changes, keyword search may fail.
That lowers recall.
'''
# Example:
# Query: "How to invert a list?"
# Doc: "How to reverse a list?"
# No shared word → possible miss



'''
Q4. How does semantic search work?

A.
It converts text into embeddings (vectors).
Then it compares vectors using similarity.
If meanings are close, they are retrieved.
'''
# Example:
# Query embedding close to
# "reverse python list" embedding
# → retrieved even without shared words



'''
Q5. Why is semantic search better for natural language questions?

A.
Because it captures intent.
It understands paraphrases and flexible wording.
That improves recall.
'''
# Example:
# "Ways to improve sleep"
# Retrieves "sleep hygiene practices"



'''
Q6. What is recall and why does semantic search improve it?

A.
Recall means how many relevant documents
are successfully retrieved.
Semantic search improves recall
by capturing meaning instead of exact words.
'''
# Example:
# 10 relevant docs exist
# Keyword retrieves 3
# Semantic retrieves 8
# Higher recall



'''
Q7. What are the trade-offs of semantic search?

A.
It requires:
- Embedding model
- Vector database
- More infrastructure
It is more complex than keyword search.
'''
# Example:
# Need embedding pipeline + ANN index



'''
Q8. Why do modern RAG systems use hybrid retrieval?

A.
Because keyword search gives precision (exact matches),
and semantic search gives recall (meaning matches).
Together they improve retrieval quality.
'''
# Example:
# Exact term match + semantic similarity
# → More reliable context for LLM



'''
Q9. What does retrieval quality directly affect in RAG?

A.
It directly affects generation quality.
Bad retrieval → bad context → bad answer.
'''
# Example:
# Wrong chunk retrieved
# LLM confidently answers incorrectly



'''
Q10. Interview-ready summary of the difference:

A.
Keyword search relies on lexical overlap,
while semantic search relies on embedding similarity.
Modern RAG systems combine both to balance precision and recall,
ensuring high-quality context retrieval for grounded generation.
'''
# Example:
# Hybrid retrieval → better answers
