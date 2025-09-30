# Variablas - A Container for a value (String, integer, float, boolean)
#               A variable behaves as if it was the value it cointains

# Strings
first_name = "Baki"
food = "Durum"
status = "student"
email = "BigD@gmail.com"

print(first_name) # important not use use qoutes " ". coz then you're printing the string...
                    # not what the string is assigned to

#if you want to use your variable along with some text. then you use a formatted string(f-string)
print(f"Hello {first_name}")
print(f"you like {food}, because youre a {status}")

# Integers
age = 29
quantity = 3
num_of_students = 30
# Floats
price_of_cakes = 5.99
GPA = 7,5

print(f"you're {age} years old")
print(f"you're buying {quantity} cakes for {num_of_students} students, its going to cost you {price_of_cakes} each")

# Boolean (in generelt its going to be easier if you ask yourself that question first)
is_student = False #Always Capital
for_sale = True

if is_student:
    print("your are a student") #Assign True
else:
    print("your are gay...") #Assign False


#Changing Case in strings
name = "ada lovelace"
print(name.title())
#The output will be 'Ada Lovelace' despite we not using a upper case. does python change it for us

name = "Ada Lovelace"
print(name.upper()) #Makes everything uppercaps
print(name.lower()) #Makes everything lowercaps

# full names
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello {full_name.title()}!")


# white spaces
# use \t for tab
print("\tPython")
# use \n for newline
print("Languages:\nPython\nC\nJavascript")
# Can also be combined
print("Languages:\n\tPython\n\tC\n\tJavascript")


# Removing prefix
    #good for Removing prefixes in URLs
nostarch_url = "https://nostarch.com"
nostarch_url.removeprefix("https://")
print(f"{nostarch_url}") # nostarch.com is the result







