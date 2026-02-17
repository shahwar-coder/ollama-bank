'''
Sensitive Information in AI Systems

1. Can't give sensitive info to third-party APIs
   - If you send private company data to a cloud model,
     it leaves your system.
   - This creates security and compliance risks.
   - Example:
       Customer database
       Financial reports
       Internal strategy documents

2. Can't make such info public
   - Proprietary data must remain confidential.
   - Legal and business consequences can occur if leaked.
   - Some industries (healthcare, finance, defense)
     have strict data regulations.

Why Local AI Helps:

- Data stays on your own machine/server.
- No external transmission.
- Full control over who accesses it.

Simple Mental Model:

Sensitive Data → Should stay inside your walls.
Cloud API → Sends data outside your walls.
Local Model (Ollama) → Keeps data inside your walls.
'''
