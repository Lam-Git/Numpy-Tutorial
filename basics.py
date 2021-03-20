import numpy as np

# basics
a = np.array([1, 2, 3], dtype="int32")
print(a)

# output-------->[1,2,3]

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

# output-----> [[9. 8. 7.][6. 5. 4.]]

# Get Dimension
print(a.ndim)
# output-----> 1
print(b.ndim)
# output-----> 2


# Get Shape
print(b.shape)
# output-----> (2,3)

# Get Type
print(a.dtype)
# output -----> int32

# Get Size
print(a.itemsize)
# output ----->4

# Get total size
print(a.nbytes)
# output ----->12

# Get number of elements
print(a.size)
# output-----> 3
