# python compound interest calculator
# Formular = P(1+r/n)^t

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle cant be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate cant be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("time cant be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years/s: ${total:.2f}")




