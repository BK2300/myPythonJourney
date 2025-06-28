# Typecasting = the process of converting a value to one datatype to another
#       (string, int, float, boolean)
#        Explicit vs implicit

name = "Baki"
age = 29
gpa = 7.5
student = True

# shows us what type of variable the assign variable is.
#print(type(name))
#print(type(age))
#print(type(gpa))
#print(type(student))

age = float(age) #our age was a int, now its a float
print(type(age))    #and this line proves it to us.

# its really good to use concatenate between string and boolean to see if someone inputtet their name or not
name = bool(name)
print(name)
# the result will always be true. But onjly if " " is empty. Its will show false.