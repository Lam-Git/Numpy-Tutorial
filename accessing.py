import numpy as np

# 2 deminational
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

# output---> [[ 1  2  3  4  5  6  7][ 8  9 10 11 12 13 14]]

# Get a specific element [row, column]
# a[row 1, column 5]
print(a[1, 5])
# output---> 13

# Get a specific row
# a[row 0, column (entire : )]
print(a[0, :])
# output----> [ 1  2  3  4  5  6  7]

# Get a specific column
# skip the row but its going to pick index 2 from each array
print(a[:, 2])
# output ----> array([ 3, 10])

# Getting a little more fancy [startindex:endindex:stepsize]
# "Row 0, index 1, backward 1, skip by 2"
print(a[0, 1:-1:2])
# output ---> ([2, 4, 6])

# replace an index , so from the original
# output---> [[ 1  2  3  4  5  6  7][ 8  9 10 11 12 13 14]]
# 20 is going to replace 13
a[1, 5] = 20
print(a)

a[:, 2] = [1, 100]
print(a)

b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)
