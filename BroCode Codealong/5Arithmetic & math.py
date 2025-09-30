import math

    # Basic arithmetic operators
friends = 5
# friends = friends + 1 #incremente by one
# friends += 1 #this is an 'augmented operators python'
# friends = friends - 2
# friends -= 2
# friends = friends - 3
# friends *= 3
# friends = friends / 4
# friends /= 4
# friends = friends ** 2 # ** is like saying 'to the power of x'. just like ^x
# friends **= 2
# remainder = friends % 3 #This is called 'modulus'. is like the remaining about of friends, which is 2
print(friends)

x = 3.14
y = 4
z = 5

# result = round(x) #rounding to the nearest int.
# result = abs(y) #abs stands for the absolute value of x.
# result = pow(4, 3) #'power of' with a base and a exponent. like saying '4 * 4 * 4' here, which is 64
# result = max(x, y, z) # the maximum or highest value of the our three parameters.
# result = min(x, y, z) # the manimum or lowest value of the our three parameters.
# print(result)


# print(math.pi) #this is how to get the value of pi
# print(math.e) #this is mostly used for physics student
# result = math.sqrt(x) #here we find the square root of x (the same variable from before
# result = math.ceil(x) #ceil will always round a float up, to the closest integer.
# result = math.floor(x) #floor will always round a float down, to the closest integer.
# print(result)


# exercise 1
    # calculate the circumference of a circle
        # formular C = 2 * pi * r

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}") #here we get a really long number
                                  #thefore we use 'round'. and ', 2' for only giving us 2 decimals

# exercise 2
    # Calculate the area of a circle
radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")


# exercise 3
# Pythagorean theorem (formula == c = square root of a2 + b2)

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c} ")