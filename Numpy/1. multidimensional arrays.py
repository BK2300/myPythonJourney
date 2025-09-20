import numpy as np

# array = np.array("A") #this is a zero dimensional array

# array = np.array(["A", "B", "C" , "D"]) #this is now a single dimensional array. like a single row

# array = np.array([["A", "B", "C"],
#                  ["D", "E", "F"],
#                  ["G", "H", "I"]]) #this is a 2 dimensional array

array = np.array([[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
                  [["J", "K", "L"], ["M", "N", "O"], ["O", "P", "Q"]],
                  [["R", "S", "T"], ["U", "V", "X"], ["Y", "Z", "_"]]]) #this is a 3 dimensional array
# We ran out of Letter. this will give us a error. We need a concisten amount of letters in each element

print(array.ndim) #ndim mean "number of dimensions" of our array
print(array.shape) #this gives us access to the shape of the attribute. first number will give you "the depth (like oberservations). the number of rows. the number of columns"

# with a python list, you would access a list like this to get "A".
# print([0],[0],[0]) #this is called "chain-indexing". good to play with it.

# But with numpy, instead of chain indexing. we have access to something called "multidimensional indexing"
# print([0, 0, 0]) # give "A" again like the previous.
# print([1, 1, 2]) # would give "O"


    ### excercise ###

#let us try to write a word now ASHE. And maybe a lastname also
# remember. first depth. rows. then column
word = array[0, 0, 0] + array[2, 0, 1] + array[0, 2, 1] + array[0, 1, 1]
last_name = array[0, 1, 0]

print(word + " " + last_name)




