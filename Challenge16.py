import numpy as np

# simple example embeddings (each row = one sentence)
embeddings = np.array([
    [0.8, 0.2, 0.6],
    [0.7, 0.3, 0.5],
    [0.2, 0.9, 0.4]
])

print("\nEmbedding Matrix:")
print(embeddings)

# show shape (rows, columns)
print("\nMatrix Shape:")
print(embeddings.shape)

# Dot product between first two vectors
dot_value = np.dot(embeddings[0], embeddings[1])
print("\nDot Product (Vector 1 · Vector 2):")
print(dot_value)

# Matrix multiplication
result = embeddings.dot(embeddings.T)

print("\nMatrix Multiplication Result:")
print(result)