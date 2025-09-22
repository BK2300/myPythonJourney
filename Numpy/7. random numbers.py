# using NumPy we might want to use random numbers.
# could be useful for simulations, modeling, applying random transformations and testing purposes.

import numpy as np

#imagen we want to roll a six-sided dice.
rng = np.random.default_rng(seed = 1) #remove "seed" if you dont want the numbers to reproduce the same result

#the third number is the amount of numbers you want to be displayed.
# the random numbers will be stored in a 1D array on default.
    # print(rng.integers(1, 7, 1000)) #this is a built-in method of integers. (remember the second number is exclusive)

# if we want a 2D array, we need to set the dimensions in size like this (in rows, then columns)
print(rng.integers(1, 7, (5, 10)))


   ## floatingpoint numbers ##

np.random.seed(seed=1) #again. its been reproduced because of "(seed=1)". just remove the "seed=1" and let ( ) stay empty
#this gives us a random floatingpoint number between zero and one by default. but you can set a range:
print(np.random.uniform(-1, 1, (3, 3))) #the uniformed method means uniformed distribution. meaning each value has a equal chance to be selected


    ## shuffling an array

rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array) #randomly shuffles our number without a coherent order
print(array)

    # lets try with some items, can gives us a random choice:
fruits = np.array(["apple", "banana", "orange", "coconut", "pineapple"])
fruits = rng.choice(fruits, size=(3, 3)) #this could be a slots machine
print(fruits)



