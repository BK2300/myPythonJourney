# indexing = accessing elements of a sequance using [] (indexing operator)
#            [start : end : step]
#            (Typically seen with credits cards)

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# with other words. we tried to find out whats the first index is, in this given creditcard number
# could imagen its good, if this was inputted into a system and we need a if-statement
# to find out if this is a foreign valid creditnumber from DK or foreign

# print(credit_number[0:10])
#this mean, "show me the first five numbers". and i guess it removes "-" automatically.
# print(credit_number[5:9])
# the index means, numbers between 5 and 9 (5678)
# print(credit_number[5:])
# the index means, numbers every number from the fifth number. so index group 2, 3, 4 (xxxx-'5678-9012-3456')

### Negative index
# print(credit_number[-3])
# this just tells python to start from right to left. or backwards with the numbers

### Step
# print(credit_number[::2]) #result "13-6891-46"
# this just meant, python took every second number or input from the creditcard number

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
# This one, you usually see when you go to a website and they ask you, does your card number end with 1234?

