'''
Q1. What does it really mean when we say “a word is a point in space”?

A.
It means the word is converted into a list of numbers.
Those numbers act like coordinates.
Just like (2,3) is a point in 2D,
an embedding like [0.12, -0.8, 0.33, ...] is a point in high-dimensional space.
'''
# Example:
# "child" → [0.12, -0.8, 0.33]
# That list of numbers = its location in meaning space



'''
Q2. Why does language become geometry?

A.
Because we convert words and sentences into vectors.
Vectors can be placed in space.
Once placed in space, we can measure distance and angle.
That turns meaning into geometry.
'''
# Example:
# Words → vectors
# Vectors → points
# Points → measurable relationships



'''
Q3. Why does closeness mean similarity?

A.
Because words that appear in similar contexts
get trained to have similar vectors.
Training pushes similar-usage words closer together.
'''
# Example:
# "child plays"
# "kid plays"
# Model learns both behave similarly
# → their vectors move closer



'''
Q4. What does “latent semantic space” mean?

A.
It means the dimensions represent hidden meaning features.
They are not labeled,
but they capture patterns like emotion, topic, or animacy.
'''
# Example:
# One hidden direction may loosely represent “animal-like”
# Another may represent “technology-related”
# We don’t name them, but they exist in math



'''
Q5. What does cosine similarity measure in simple terms?

A.
It measures how aligned two vectors are.
If they point in the same direction,
their meanings are similar.
'''
# Example:
# Vector A → ↗
# Vector B → ↗
# Cosine ≈ 1 (very similar)
# Vector C → ↘
# Cosine ≈ low (different meaning)



'''
Q6. Why do we focus on direction instead of distance?

A.
Because direction captures meaning.
Magnitude may change due to length or emphasis,
but direction represents semantic identity.
'''
# Example:
# "cat"
# "small domestic cat animal"
# Length changes, direction similar



'''
Q7. How do embeddings learn that similar words should be close?

A.
Through co-occurrence patterns.
Words that appear in similar sentences
get adjusted to have similar vectors.
'''
# Example:
# "doctor treats patient"
# "physician treats patient"
# Model learns doctor ≈ physician



'''
Q8. What does clustering in embedding space represent?

A.
It represents groups of related meanings.
Similar concepts form neighborhoods.
'''
# Example:
# Animals cluster together
# Vehicles cluster together
# Emotions cluster together



'''
Q9. Why does vector arithmetic like “king - man + woman ≈ queen” work?

A.
Because relationships are encoded as directions.
Gender difference is a consistent vector direction.
So shifting along that direction changes meaning.
'''
# Example:
# king → royal + male
# remove male
# add female
# → queen



'''
Q10. Interview-ready explanation: How does language become geometry?

A.
Language becomes geometry when words and sentences
are mapped into high-dimensional vectors.
Semantic similarity corresponds to angular closeness
because models learn representations based on contextual usage.
This turns meaning into measurable spatial relationships.
'''
# Example:
# Text → embedding → point in space
# Similar meaning → nearby points
