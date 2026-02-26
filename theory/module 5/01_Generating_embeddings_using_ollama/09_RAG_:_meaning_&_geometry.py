'''
Q1. What does it mean to say “meaning becomes geometry”?

A.
It means text is converted into numerical vectors.
Those vectors become points in high-dimensional space.
Similar meanings appear close together.
'''
# Example:
# "cat" → vector A
# "dog" → vector B (close to A)
# "car" → vector C (far from A)



'''
Q2. Why are embeddings described as coordinates?

A.
Because each embedding is a list of numbers.
Those numbers act like coordinates in space.
'''
# Example:
# cat → (0.2, 0.9)
# dog → (0.25, 0.85)
# car → (-0.6, 0.1)



'''
Q3. What does “closeness” represent in embedding space?

A.
Closeness represents semantic similarity.
If two vectors are near each other,
their meanings are similar.
'''
# Example:
# "child" and "kid" → close vectors
# "child" and "airplane" → far apart



'''
Q4. What do embedding dimensions represent?

A.
They represent latent semantic features.
These are hidden meaning axes learned by the model.
They are not explicitly labeled.
'''
# Example:
# One dimension may loosely encode “animalness”
# Another may encode “motion”
# But not directly named



'''
Q5. Why is cosine similarity commonly used?

A.
Because cosine similarity measures the angle between vectors.
Meaning is reflected more in direction than magnitude.
'''
# Example:
# Two vectors pointing same direction → cosine ≈ 1
# Opposite directions → cosine ≈ -1



'''
Q6. Why is direction more important than magnitude?

A.
Sentence length or wording can change magnitude.
But semantic meaning is captured by direction.
Cosine similarity removes magnitude effects.
'''
# Example:
# "cat"
# "small domestic cat animal"
# Magnitude differs, direction similar



'''
Q7. What are the main steps in creating embeddings?

A.
1. Token → vector projection
2. Contextualization via transformer layers
3. Pooling into a single sentence vector
4. Similarity comparison
'''
# Example:
# Sentence → embedding model → 768D vector



'''
Q8. What is the strongest mental analogy for embeddings?

A.
Embedding space is like a semantic map.
Texts are cities.
Similar meanings are geographically close.
'''
# Example:
# Query vector → find nearest “city”
# That is nearest meaning



'''
Q9. What is the ultra-simple summary of embeddings?

A.
Text → vector → point in meaning space.
Similarity → geometric closeness.
Retrieval → nearest neighbor search.
'''
# Example:
# Ask: "How do plants eat?"
# Closest chunk → "Photosynthesis process"



'''
Q10. What is the deep final insight?

A.
Embeddings transform language into a continuous
high-dimensional space where meaning corresponds
to geometric direction and proximity.
'''
# Example:
# Analogy tasks work because relationships
# become spatial relationships in vector space
