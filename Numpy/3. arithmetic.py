    # (there is a couple different sections to this topic)
    ## ill begin with "scalar arithmetic" is a linear algebra term

import numpy as np

array = np.array([1, 2, 3])

print(array + 1) #where is where scalar arithmetic comes in. we can apply a value to each array
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5) #remember "two **" is like ^x (power of x)
print(" ")

    ## vectorized math funcs
# a vector is like a 1D list. where as a scalar is a value

array2 = np.array([1.01, 2.5, 3.99])
print(np.sqrt(array2)) #using the square root function
print(np.round(array2)) #we round up function
print(np.floor(array2)) #we ALWAYS round down function
print(np.ceil(array2)) #we ALWAYS round up function
print(np.pi) #return pi
print(" ")

    ## vectorized math functions

radiuses = np.array([1, 2, 3])
print(np.pi * radiuses ** 2) #The formular is "A = pi radius^2
print(" ")

    ##elementwise arithmetic

array3 = np.array([1, 2, 3])
array4 = np.array([4, 5, 6])

print(array3 + array4) #this will add together every single element/columns together
print(array3 - array4)
print(array3 * array4)
print(array3 / array4)
print(array3 ** array4)
print(" ")


    ## comparison operators
# for comparison operators we can create boolean arrays. filter data and use elementwise comparisons

scores = np.array([91, 55, 100, 73, 82, 64]) #these are student scores
#lets now see if any student got a perfect score

print(scores == 100) #this will return a boolean (F F T F F F). elements nr 3 got a perfect score
print(scores >= 60) #equal to or above 60 (T F T T T T)
print(scores < 60) # anybody below 60 ( F T F F F F)

#lets give the students some grades.
# order is really important here!

scores[scores <= 60] = 0 #this is a subscript operator
scores[scores >= 99] = 12
scores[scores >= 85] = 10
scores[scores >= 75] = 7
scores[scores >= 68] = 4
scores[scores >= 61] = 2
# zero is first. or else the others would override it and give a result of the points (55) instead of the grade

print(scores)
