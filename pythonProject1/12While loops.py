# while lopp = execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")
# this comand ask us to prompt our name. and if you keep pressing anything else then a string,
#   then if asks again and again until you do it correct
# carefull! if you dont have a way to stop the whileloop. your are in a infinite loop...

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"Your are {age} years old")


food = input("Enter the food your like (q to quit): ")
while not food =="q": #We made a logital operator with 'Not'
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
print("bye")


num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))
print (f"Your number is {num}")