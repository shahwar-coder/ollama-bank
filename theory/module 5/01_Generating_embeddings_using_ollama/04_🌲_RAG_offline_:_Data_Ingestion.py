'''
Q1. What is Data Ingestion in RAG?

A.
Data ingestion is the process of collecting raw documents
and bringing them into the system.
It is the first step in building the knowledge base.
'''
# Example:
# Upload PDFs
# Scrape website content
# Import database exports



'''
Q2. What types of data can be ingested?

A.
Any knowledge source such as:
- PDFs
- Websites
- Manuals
- Database exports
- Transcripts
'''
# Example:
# Company handbook PDF
# FAQ webpage
# Customer support chat logs



'''
Q3. What is the goal of data ingestion?

A.
The goal is to move raw knowledge
into the AI system so it can later be indexed and searched.
'''
# Example:
# Raw refund policy document
# → Added to RAG pipeline



'''
Q4. Why is ingestion important before embeddings?

A.
Because embeddings can only be created
after documents are collected and prepared.
No data → nothing to embed.
'''
# Example:
# No PDFs uploaded
# → Vector database remains empty



'''
Q5. What is the key design question during ingestion?

A.
"What knowledge should my AI know?"
You must define the scope of information.
'''
# Example:
# AI for HR → ingest policies, contracts
# AI for tech support → ingest product manuals



'''
Q6. What is the simple mental model of Step 1?

A.
Collect the knowledge first.
You cannot search or retrieve
what you have not stored.
'''
# Example:
# Build library before opening it to readers
