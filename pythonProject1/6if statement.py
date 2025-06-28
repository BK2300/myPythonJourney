# if = Do something only IF some condition is True
#       Else! do something else

age = int(input("Enter your age: "))

# THe ordering of the if statement is important and can be seen on the second else if statement
if age >= 18: #Greater of equal to 18.
    print("You are now signed up!")
elif age < 0: # this is a 'else if' statement, can be used as manytimes as wanted to
    print("You are trolling us, because you havent been borned yet, ahole...")

# elif age >= 100:
#    print("you are to old to sign up")
    #This one if invalid, because everthing we are going to input, is going to overwriten by the first 'if statement'
    #   therefore we need this example to be the first if statement, for it to be valid

else:
    print("You must be 18+ to sign up")


# lets try another example
response = input("Would you like some food? (Y/N): ")
if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")


# lets try another example
name = input("Enter you name: ")

if name == "": #This means, if the user didnt type in anything
    print("You did not type in anything...")
else:
    print(f"Hello {Hello}")

# lets try another example with boleans
#   a if statement will already evaluate if the statement is true or false
online = True

if online:
    print("The user is online")
else:
    print("The user is offline")