#!/usr/bin/env python
"""
Show some vector math using NumPy. 
"""
import numpy as np

# https://numpy.org/doc/stable/reference/generated/numpy.dot.html

def main():
    # Define two vectors
    vector_a = np.array([1, 2, 3])
    vector_b = np.array([4, 5, 6])

    # Calculate the dot product
    dot_product = np.dot(vector_a, vector_b)

    print(f"Vector A: {vector_a}")
    print(f"Vector B: {vector_b}")
    print(f"Dot Product: {dot_product}")

    # Calculate the cross product
    cross_product = np.cross(vector_a, vector_b)
    print(f"Cross Product: {cross_product}")

    # Find magnitude of the vectors
    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)
    print(f"Magnitude of Vector A: {magnitude_a}")
    print(f"Magnitude of Vector B: {magnitude_b}")

if __name__ == "__main__":
    main()
