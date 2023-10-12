# Import the NumPy library
import numpy as np

# Create a 1-dimensional NumPy array
a1d = np.array([1,2,3])

# Create a 2-dimensional array of ones
ones = np.ones((2,3))

# Perform operations on arrays
print(f'a1d + ones = {a1d + ones}')  # Element-wise addition
print(f'a1d * ones = {a1d * ones}')  # Element-wise multiplication

# Create 2-dimensional and 3-dimensional arrays
a2d = np.array([[1,2,3],[4,5,6]])
a3d = np.array([[[1.1,2,3,4],[1,2,3,4]],[[1.1,2,3,4],[1,2,3,4]]])

# Slicing to modify a3d shape
a3d = a3d[:2,:2,:3]

# Perform operations on a2d and a3d
print(f'a2d * a3d = {a2d * a3d}')  # Element-wise multiplication
print(f'a1d**2 = {a1d**2}')  # Square of elements in a1d
print(f'np.square(a1d) = {np.square(a1d)}')  # Alternative method for squaring elements

# Statistical operations on a1d
print(f'np.sum(a1d) = {np.sum(a1d)}')  # Sum of elements
print(f'np.max(a1d) = {np.max(a1d)}')  # Maximum element
print(f'np.min(a1d) = {np.min(a1d)}')  # Minimum element

# Calculate mean, variance, and standard deviation of a1d
mean = np.mean(a1d)
var = np.var(a1d)
std = np.std(a1d)
print(f'mean  of a1d = {mean}')
print(f'variance of a1d = {var}')
print(f'standard deviation of a1d  = {std}')

# Generate random matrices
np.random.seed(seed=0)
random_matrix1 = np.random.randint(0,10,size=(4,3))
random_matrix2 = np.random.randint(0,10,size=(4,3))

# Perform operations on random matrices
print(f'random_matrix1 = {random_matrix1}')
print(f'random_matrix2 = {random_matrix2}')

# Transpose and reshape operations
transpose = random_matrix1.T
reshape = random_matrix2.reshape(2,3,2)
print(f'transpose = {transpose}')
print(f'reshaped = {reshape}')

# Element-wise multiplication and dot product
element_wise_multiplication = random_matrix1*random_matrix2
dot_product = random_matrix1.dot(random_matrix2.T)

print(f'element wise multiplication = {element_wise_multiplication}')
print(f'dot product = {dot_product}')
