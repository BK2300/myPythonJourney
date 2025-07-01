# python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: ")) #num1 and num2 are string data types,
num2 = float(input("Enter the second number: "))
# num1 and num2 are string data types, also know as String concatenation
# therefore the input needs to be typecasted to a float or else the result will be (f.ex: 10 + 11 = 1011)

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator dummy...")