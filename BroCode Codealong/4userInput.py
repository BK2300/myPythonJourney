# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
    # gives you the chance to input something like a name or something.
    # But it cant be used for anything yet. So we assign it a variable called 'name'
print(f"Hello {name}!") #Remember we use a f-string, if you insert a variable

age = input("How old are you?: ")
print(f"You are {age} years old")

    #the input we receive is anything but a string. then it cant be used to other then a string...
    # and needs to be tyepcasted to another variable
#age = int(age) #
#age = age + 1
    # But we could also just have told python, the input is going to be a number...
    # by inserting int(), before the print. like so
    #       age = int(input("How old are you?: "))

# Exercise
    #lets find the area of a rectangle
    # again. the number needs to be typecasted before been useale. So we convert them to a int,float or double
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The are of the rectangle is:{area} cm^2")


#Exercise 2
    #shpping cart program
item = input("What item would you like to buy today?: ")
price = float(input("What is the price of that item?: ")) #here we typecasted it to a float again, since prices often have decimals points
quantity = int(input("How many would you like to buy?: ")) #this time is typically whole numbers, so we use int
total = price * quantity

print(f"you have brought a total of {quantity} x {item}/s")
print(f"The price is going to be {total}")




