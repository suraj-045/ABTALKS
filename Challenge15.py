import numpy as np

# Correct way to store long text
sentences = [
"""Artificial intelligence is rapidly transforming modern industries by improving automation, data analysis, and decision making.
Many companies are using machine learning systems to understand customer behavior, reduce manual work, and increase productivity.
As technology continues to evolve, organizations focus on building smarter solutions that can learn from data and adapt to real-world challenges."""
]

# Simple Embeddings 
embeddings = np.array([
    [0.8, 0.2, 0.6],
    [0.7, 0.3, 0.5],
    [0.2, 0.9, 0.4]
])

print("\nEmbedding Matrix:")
print(embeddings)

print("\nMatrix Shape (rows = sentences, columns = dimensions):")
print(embeddings.shape)

# Dot Product
dot_product = embeddings.dot(embeddings.T)
print("\nDot Product Matrix:")
print(dot_product)

# Cosine Similarity
norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
cosine_sim = dot_product / (norms * norms.T)

print("\nCosine Similarity Matrix:")
print(cosine_sim)

# Mean Embedding
mean_embedding = embeddings.mean(axis=0)
print("\nMean Embedding:")
print(mean_embedding)