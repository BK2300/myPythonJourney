# Variablas - A Container for a value (String, integer, float, boolean)
#               A variable behaves as if it was the value it cointains

# Strings
first_name = "Baki"
food = "Durum"
status = "student"
email = "BigD@gmail.com"

print(first_name) # importan not use use qoutes " ". coz then you're printing the string...
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

# Boolean (in generelt its going to be easier if you ask yourself that vquestion first)
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


