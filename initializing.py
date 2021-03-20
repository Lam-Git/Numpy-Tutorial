import numpy as np

# All 0s matrix
# two rows and three column of zeros.
print(np.zeros((2, 3)))
# outputarray([[0., 0., 0.],[0., 0., 0.]])

# All 1s matrix
# Four rows, two column and two deminational
print(np.ones((4, 2, 2), dtype="int32"))

# output----->
#   ([[[1, 1],[1, 1]],
#   [[1, 1],[1, 1]],
#   [[1, 1],[1, 1]],
#   [[1, 1],[1, 1]]])

# Any other number
# 2x2 with the value
print(np.full((2, 2), 72))
# output------>
#   [[72 72]
#   [72 72]]

# Random decimal numbers
# 4x2
print(np.random.rand(4, 2, 3))
# output---->
#   ([[0.07805642, 0.53385716],
#   [0.02494273, 0.99955252],
#   [0.48588042, 0.91247437],
#   [0.27779213, 0.16597751]])


# Random Integer values
# Random number ranging from -4-8 with the size 3x3
np.random.randint(-4, 8, size=(3, 3))
# output----->
#   ([[-2, -4, -4],
#    [ 6,  6,  3],
#    [ 3,  2,  2]])


# The identity matrix
np.identity(5)
#   ([[1., 0., 0., 0., 0.],
#   [0., 1., 0., 0., 0.],
#   [0., 0., 1., 0., 0.],
#   [0., 0., 0., 1., 0.],
#   [0., 0., 0., 0., 1.]])

# Repeat an array
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)
