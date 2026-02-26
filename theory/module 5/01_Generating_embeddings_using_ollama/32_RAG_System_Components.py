'''
Typical RAG System Components (Refined Concise)

1️⃣ Data loader
- Ingests raw sources (PDFs, web, docs)

2️⃣ Chunker
- Splits large text into smaller retrievable units

3️⃣ Embedding model
- Converts chunks into semantic vectors

4️⃣ Vector database
- Stores embeddings with documents for similarity search

5️⃣ Retriever
- Finds top-k relevant chunks for a query

6️⃣ Prompt builder
- Combines query + retrieved context into final prompt

7️⃣ LLM generator
- Produces grounded answer using prompt context

⭐ Summary:
Ingest → Chunk → Embed → Store → Retrieve → Prompt → Generate
'''