import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
# output -----> ([1 2 3 4])

a + 2
# output----> ([3, 4, 5, 6])

a - 2
# output-----> ([-1,  0,  1,  2])

a * 2
# output-----> ([2, 4, 6, 8])

a / 2
# output-----> ([0.5, 1. , 1.5, 2. ])

b = np.array([1, 0, 1, 0])
a + b
# output -----> ([1, 0, 3, 0])

a ** 2
# output-----> ([ 1,  4,  9, 16], dtype=int32)

# Take the sin
np.cos(a)
# output-----> ([ 0.54030231, -0.41614684, -0.9899925 , -0.65364362])
# -------------Linear Algebra--------------------
a = np.ones((2, 3))
print(a)

b = np.full((3, 2), 2)
print(b)

np.matmul(a, b)
# output---for both (a)/(b)
#   [[1. 1. 1.]
#   [1. 1. 1.]]
#   [[2 2]
#   [2 2]
#   [2 2]]

# final output
#   ([[6., 6.],
#   [6., 6.]])

