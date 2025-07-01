# format specifiers = {:flags} ('= this is a flag. Remember from the input value from the f"String')
#                               format a value based on what, flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate vvand zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate postive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 12345.67
price5 = 10000.00

print(f"Price 1 is ${price1:.2f}") #Example 1. we only want 2 decimal numbers to show
print(f"Price 2 is ${price2:.2f}")

print(f"Price 2 is ${price2:10}") #makes it looking clean. Like creating a wall and the numbers lean against them
print(f"Price 3 is ${price3:10}")

# print(f"Price 2 is ${price2:010}") #is you add a 0. the empty spaces vill becomes zeros
# print(f"Price 3 is ${price3:010}") #saw it irrelevant, so i removed it. but you can test it yourself

print(f"Price 2 is ${price1:<10}") #these nubmers are left justified. so the empty spaces comes after the numbers.
print(f"Price 3 is ${price3:<10}") #(try to print and click after the number assigned)

print(f"Price 2 is ${price1:>10}") #looks the same af example 2
print(f"Price 3 is ${price3:>10}")

print(f"Price 3 is ${price3:^10}") #the numbers are now centered
print(f"Price 1 is ${price1:^10}")

print(f"Price 1 is ${price1:+}") #if you have a positive value. and want a plus sign in front
print(f"Price 2 is ${price2:+}")

print(f"Price 1 is ${price1: }") #if you have a positive value. and dont want anything in front
print(f"Price 2 is ${price2: }")

print(f"Price 4 is ${price4:,}") #thousands are seperated with a comma
print(f"Price 5 is ${price5:,}") #makes sure there is no space after the comma!
print(f"Price 4 is ${price4:+,.2f}") #we want a plussign in front. with a thousand seperator and 2 decimal points
print(f"Price 5 is ${price5:+,.2f}")

