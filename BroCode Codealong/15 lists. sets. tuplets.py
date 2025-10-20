# collection = single "Cariable" used to store multiple values
#     List   = [] ordered and changeable. Duplicates OK
#     Set    = {} unordered and immutable, but Add/Remove OK. No duplicates
#     Tuples = () ordered and unchangedable. Duplicates OK. Faster


# fruits = ["Apple", "Banana", "Orange", "Coconut"]
    # fruits[1] = "Pineapple" #This reassigns the apple
    # fruits.append("Pineapple") #adds pineapple to the end
    # fruits.remove("Apple")
    # fruits.insert(0, "pineapple") #You telling it, you want to insert pineapple in place 0
    # fruits.sort() #Now are they in alphabetical order
    # fruits.reverse() #fruits are reversed in order we placed them
        # if you want to 'sort' and then 'reverse'. you have to do it separately
    # fruits.clear() #removes all the values
    # print(fruits.index("Orange")) #this show where the orange is
    # print(fruits.count("Banana")) #this shows how many there is of x

    # print(fruits[0:3]) #shows only between first value to third value. remember second number is exclusive

# for fruit in fruits: #we used 'for x' before. we can still do that.
#      But the common if your variable is plural. you do x as singlural
#      print(fruit)

    # If you want to see all the different methods you can use in a collection. Use dir()
# print(dir(fruits)) #shows a bunch on attributes, important for Data science
    # if you want a description of each methods. try this:
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)



# fruits = {"Apple", "Banana", "Orange", "Coconut", "Coconut"}
    #this time the order is randomized when printing
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits[0]) # doesnt work, since its randomized

    # fruits.add("pineapple") #but we can still add
    # fruits.remove("Apple")
    # fruits.pop() #removed first element. but still random
    # fruits.clear() #the elements of our value is gone


fruits = ("Apple", "Banana", "Orange", "Coconut", "Coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

print(fruits.index("Apple"))
print(fruits.count("Coconut"))
