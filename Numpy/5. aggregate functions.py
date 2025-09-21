# aggregate functions = summarize data and typically return a single value

import numpy as np

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

# print(np.sum(array)) #combinate result added together
# print(np.mean(array)) #the average value is 5.5
# print(np.std(array)) #standard deviantion
# print(np.var(array)) #variance
# print(np.min(array)) # minimum value
# print(np.max(array)) #max value
# print(np.argmin(array)) #"arg" stands for argument. finds the position of the minimum value (this function will return the index number 0)
# print(np.argmax(array)) #index number 9
# print(np.sum(array, axis=0)) # this is summing/adding all the columns together (so [7 9 11 13 15])
# print(np.sum(array, axis=1)) # we change from 0 to 1. This is summing/adding all the rows together (so [15 40])











