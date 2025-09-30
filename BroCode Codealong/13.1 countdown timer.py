import time

my_time = int(input("Enter the time in seconds: "))

# for x in range(0, my_time):
#    print(x) # x is whatever the count time is. so 1, 2, 3, n...
#    time.sleep(1) #Seconds its counting down with
# print("Time's up!")

#There is two way to make it count backwards.
# U can use the first one on top and add reverse() in front. or
# You can take your my_time, end timer at 0 and step which is the third number(called step)

for x in range(my_time, 0, -1): #Step
# modules (%) is our limiter. so if we had days. we could add % 24 after hours for days
    seconds = x % 60 #we only asked for seconds. so we cant make it higher then 60. or else it only starts over again
    minutes = int(x / 60) % 60
    hours = int(x / 3600) #3600 is the amount of seconds in an hour
    print(f"{hours:02}:{minutes:02}:{seconds:02}") #Here we added format specifiers. so it shows 2 degits.
# like number below 10. will add a 0 in front, to make it look better
    time.sleep(1)

print("Time's up!")


