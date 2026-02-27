import numpy as np
from scipy.optimize import minimize

# Step 1: Text Representation (Embedding Vectors)
# Example: two sentence embeddings (manual)
vector1 = np.array([0.9, 0.1, 0.7])
vector2 = np.array([0.3, 0.8, 0.4])

print("\nOriginal Vectors:")
print("Vector 1:", vector1)
print("Vector 2:", vector2)

# Step 2: Define Cost Function
# We want vector2 to become closer to vector1
# So we minimize squared distance
def cost_function(v):
    return np.sum((v - vector1) ** 2)

# Step 3: Cosine Similarity Function
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

before_similarity = cosine_similarity(vector1, vector2)
print("\nCosine Similarity Before Optimization:")
print(before_similarity)

# Step 4: Apply SciPy Optimization
result = minimize(cost_function, vector2)

optimized_vector = result.x

print("\nOptimized Vector2:")
print(optimized_vector)

# Step 5: Similarity After Optimization
after_similarity = cosine_similarity(vector1, optimized_vector)

print("\nCosine Similarity After Optimization:")
print(after_similarity)