# filtering = refers to the process of selecting elements from an array that match a given condition

import numpy as np

# imagen a two group of people taking night classes and we need their ages.
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) | (ages < 65)]#usually we use "and" in logical operators. But NumPy uses c style arrays, so we have to use "an amperand = &".
# if we used "or = |". then we would target the range outsite of 18 and 65. but the < > sumbols også have to change too.
seniors = ages[ages >= 65]
even_age = ages[ages % 2 == 0] #modulus gives us the remainder of any division
odd_age = ages[ages % 2 != 0] #"1=" means does not equals zero

# when filtering and creating a new array and want to preserve the original shape:
#there is tree arguments. the first is our condition. the second is our array. the third is a fill value.
adults2 = np.where(ages >= 18, ages, 0) #zero is replacing the value. so anybody below 18, will be replaced to zero


print(teenagers) #we have tree teenagers in both groups. This is boolean indexing
print(adults) #we get 11 adults, that is between 18 and 65
print(seniors) # we have a age of 65 and 99
print(even_age)
print(odd_age)
print(adults2)













