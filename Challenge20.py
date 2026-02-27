import numpy as np

# Step 1: Create Embedding Vectors
vector1 = np.array([0.5, 0.8, 0.2])
vector2 = np.array([0.6, 0.7, 0.3])

print("\nVector1:", vector1)
print("Vector2:", vector2)

# Step 2: Validate Shape
if vector1.shape != vector2.shape:
    print("Error: Vectors must have same dimensions.")
    exit()

# Step 3: Cosine Similarity Function
def cosine_similarity(a, b):
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    # handle zero division case
    if norm_a == 0 or norm_b == 0:
        return 0

    return np.dot(a, b) / (norm_a * norm_b)

similarity = cosine_similarity(vector1, vector2)

print("\nCosine Similarity:", similarity)

# Optional: Euclidean Distance
distance = np.linalg.norm(vector1 - vector2)
print("Euclidean Distance:", distance)

# Step 4: Interpretation
if similarity > 0.8:
    print("Interpretation: Vectors are highly similar.")
elif similarity > 0.5:
    print("Interpretation: Vectors are moderately similar.")
else:
    print("Interpretation: Vectors are not very similar.")