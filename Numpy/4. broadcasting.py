# broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger arrays's shape

# the dimensions have the same size
# OR
# one of the dimensions has a size of 1.

import numpy as np

array1 = np.array([[1, 2, 3, 4], #this is a 2D array
                   [5, 6, 7, 8], #suddenly we have two rows. and it nether matches the number, nor is a 1.
# but if we had two more rows. they suddenly do match:
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
array2 = np.array([[1], [2], [3], [4]]) # this is a 2D array too. But it has 4 columns, but only one row
# if i added a random number extra in array2. the numbers will not match anymore

print(array1.shape) #result (4, 1)
print(array2.shape) #result (1, 4)

print(array1 * array2)

    ## excercise

array3 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array4 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array3.shape) #result (1, 10)
print(array4.shape) #result (10, 1)

print(array3 * array4)