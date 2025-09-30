
# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")

# result = len(name)
    # this returns an integer with the length of the input (in this situation the inputted name length
# result = name.find(" ")
    # this method show where the 'space' is between the string.
    # the first letter is Zero and the the output will be -1, if there is no 'spaces'
# result = name.rfind("o")
    # finds the last 'o' in the string. good for if you have multiple o's in a string

# name = name.capitalize() #Caps the first letter, if the user forget
# name = name.upper() #Caps all the inputed letters
# name = name.lower()
# name = name.isdigit()
    #this is a boolean, returns true if its digits/numbers only. A mix if letters and numbers will still be false
# name = name.isalpha()
    # same. but only letters from the alphabet. means no spaces, or the result still false

# result = phone_number.count(" ")
# result = phone_number.replace("6", "9")
    # this one replaces all to another. like here ive done the sixes to nines. to troll somebody

# print(result)


### Exercise time!
# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

# task 1
if len(username) > 12:
    print("your username cant be more than 12 characters")
# task 2
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
# task 3
elif not username.isalpha():
    print("your username cant contain numbers")
else:
    print(f"Welcome {username}")



