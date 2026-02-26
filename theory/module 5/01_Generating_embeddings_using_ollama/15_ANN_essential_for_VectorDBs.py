'''
Q. Why ANN is essential for Vector Databases

Without ANN:
👉 A vector database becomes useless at scale

Because:
- Brute-force similarity search is O(N)
- Every query compares against all stored vectors
- Latency grows linearly with data size → very slow

ANN provides:
- Smart search over promising regions only
- Avoids scanning entire dataset
- Achieves near O(log N)–style behavior

👉 Result:
Fast, scalable similarity search for millions/billions of vectors
'''