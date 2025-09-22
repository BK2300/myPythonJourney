# series = A series is a Pandas 1D labeled array that can hold any data type.
#             Think of it like a single column in a spreadsheet or a single variable in a data matrix

import pandas as pd

data = [100, 102, 104, 200, 202] #fictive data frame

series = pd.Series(data, index=["a", "b", "c", "d", "e"]) #Series is a constroctor and not a function. therefore it have to be uppercase
#the index start by default on 0,1,2. so we gave it a index label

#series.loc["c"] = 200 #we just changed the value of our dataframe

print(series)
print(series.loc["a"]) #loc = location. this returns the value of label "a"
print(series.iloc[0]) #iloc shows the integer location. which is the same as a like before
print(series[series >= 200]) #meaning be filter by value, that is equal or greater than 200.
print()

# lets us try to make a dictionary

calories = {"day 1": 1750, "day 2": 2100, "day 3": 1700}

series = pd.Series(calories) #since our dictionary is made up of "key-value pairs". well use the keys as the labels

print(series)
print(series[series >= 2000]) #this one day did i cheat on my diet.
print(series[series < 2000]) #these two day did i stick to my diet.




