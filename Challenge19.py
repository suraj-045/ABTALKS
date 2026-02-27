import numpy as np

# Step 1: Generate Embedding Vectors
vector1 = np.array([3.0, 4.0, 0.0])
vector2 = np.array([1.0, 2.0, 2.0])

print("\nOriginal Vectors:")
print("Vector1:", vector1)
print("Vector2:", vector2)

# Step 2: Cosine Similarity Function
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

before_similarity = cosine_similarity(vector1, vector2)
print("\nCosine Similarity Before Normalization:")
print(before_similarity)

# Step 3: L2 Normalization (Safe)
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:        # numerical stability check
        return v
    return v / norm

norm_v1 = normalize(vector1)
norm_v2 = normalize(vector2)

print("\nNormalized Vectors:")
print("Normalized Vector1:", norm_v1)
print("Normalized Vector2:", norm_v2)

# Step 4: Similarity After Normalization
after_similarity = cosine_similarity(norm_v1, norm_v2)

print("\nCosine Similarity After Normalization:")
print(after_similarity)