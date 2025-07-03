# for loops = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc.

#for x in range(1, 11): # the second number is exclusive(11), so we need to add +1
#    print(x)
# print("Happy new Year!")

# for x in reversed(range(1, 11, 2)): #reversed countdown backwards. and the third number is counting every second number

# credit_card = "1234-5678-9101-1121"

#for x in credit_card:
#    print(x)


### two usefull keyword = continue and break

for x in range(1, 21):
    if x == 13:
        continue #The continue keyword skips over a number
#       break # stops at 13.
    else:
        print(x)


