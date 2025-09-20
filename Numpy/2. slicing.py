import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# Row selection
# array[start:end:step] #the ending index is exclusive, meaning you have to add one extra in for it to match up
# print(array[::]) #if we leave the columns empty. the will omit
# print(array[::2])
# print(array[::-1]) #will return all the rows in reverse

# Column selection
# array[0, 0] the first index is for the column. the second is for the row

# print(array[:, 0]) #this gives us all the rows from start to finish. But the first columns in each row
# print(array[1:3, 2]) #this gives us second and third row. But the third number columns in each row

# print(array[:, 0:3]) #this will print all rows. but the first three columns in each row
# print(array[:, 1:]) #this will print all rows. But skip the first column. here we omit the ending column. its the same as writing 4 there
# print(array[:, 1::2]) #print all rows. starting at the second number in and gives us every second number

# print(array[0:2: , 0:2]) #print first two columns, of the first two rows
print(array[0:2: , 2:5]) #print two last numbers of the first two rows. we could also omit the number 5



