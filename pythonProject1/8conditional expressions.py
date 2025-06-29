# conditional expression = A one-line shortcut for the id-else statement (ternary operator)
#                     Print or assign of two based on a condition
#                     X if condition Y


num = 5
a = 6
b = 7
age = 10
temperature = 30
user_role = "guest"


# print("Positiv" if num > 0 else "Negative")
# result = "Even" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
        #  #this line says "return variable A, if a is greater then B. Else then return B
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full access" if user_role == "admin" else "Limited Access"

print(access_level)



