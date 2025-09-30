# nested loop = A Loop within another loop (outer. inner)
# (example)     outer loop:
#                    inner loop:
#you'll encounter them with "while loop" inside a "while loop". "for loop" inside a "for loop"
#   While inside for and for inside a while etc.

# for x in range(1, 10):
#     print(x, end=" ") # that 'end=""' means the numbers goes in a horizontal instead of a vertical
#         # the empty space is what goes between the numbers. so a - or sometime could be usefull

# for x in range(3): #this mean the code with be executed 3 times
#     for y in range(1, 10):
#         print(y, end=" ")
#     print() # this prints a empty line after the previous command was done. Therefore its looks like you\ve created a new line

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print() # this prints a empty line after the previous command was done. Therefore its looks like you\ve created a new line





