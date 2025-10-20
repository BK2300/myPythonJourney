# functions = A block of reusable code
#             Place () after the function name to invoke it
# return = statement used to end a function
#          and send a result back to the caller

# to define a function. you'll type 'def'
def happy_birthday(name, age): #this is a parameter. It's like a temporary variable thats used within a function. ORDER DOES MATTER!
    print(f"Happy birthday to {name}") #We replaced you with our parameter
    print(f"You are {age} years old!")
    print("Happy birthday to you")
    print()

#its important when you passing in an argument, u need to have a matching set of parameters
happy_birthday("Bro", 15) #This is a argument, sending values directly to a function
happy_birthday("Steven", 30)
happy_birthday("Kevin", 40)

    #__________________________

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}") #after amount, we used a format specifier
    print()

display_invoice("Billy", 42.50, "01/02")


    # __________________________

def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divided(x,y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divided(1,2))
print()

    # __________________________

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last #We concatenated these strings together

full_name = create_name("baki", "tuski")

print(full_name)
