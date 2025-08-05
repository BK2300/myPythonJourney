# 2d lists = a list of a lists

    # imagen if you had its set up as rows and colums
fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrot", "potatos"]
meats =      ["chicken", "fish", "turkey"]
groceries = [fruits, vegetables, meats]

    #this works too (look closely to ekstra commas and square brackets)
# groceries =     [["apple", "orange", "banana", "coconut"],
#                 ["celery", "carrot", "potatos"],
#                 ["chicken", "fish", "turkey"]]

# print(groceries[0][0]) #first square bracket = rows. second square bracket = columns
for collection in groceries: #nested loops
    for food in collection:
        print(food, end= " ") #print(food) alone is vertical. end= " " makes it horizontal
    print() #suddenly makes it a grid looking. like above

print(f"\n") #just an extra to seperate the lesson from the exercise

    ### quick exercise
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ('*', 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()


