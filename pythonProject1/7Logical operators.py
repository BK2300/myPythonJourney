# logical operatrs = evalute multiple condition (or, and, not)
#               or = at least one condition must be true
#              and = both conditions must be True
#              not = inverts the condition (not false, not True)

# OR
# temp = 25
# is_raining = False

# if temp > 35 or temp < 0 or is_raining: #if atleast one of these conditions are true. The this going on
#    print("The outdoor event is cancelled")
# else:
#    print("The outdoor event is still scheduled")

# AND
temp = 5
is_sunny = True

if temp >= 25 and is_sunny: #For this condition to be true. both operators must be true.
    # therefor can a temp on 24 and below not be true
    print("It is HOT outside🥵")
    print("Its is sunny🌞")
elif temp <= 0 and is_sunny: #here temp is changed to 0 or less
    print("It is COLD outside🥶")
    print("Its is sunny🌞")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside😎")
    print("Its is sunny🌞")
# now we play around with the "NOT" condition too.
#It inverts our condition. like our boolean. so its true here. then his check for the opposite
elif temp >= 25 and not is_sunny: #For this condition to be true. both operators must be true.
    # therefor can a temp on 24 and below not be true
    print("It is HOT outside🥵")
    print("Its is CLOUDY☁")
elif temp <= 0 and not is_sunny: #here temp is changed to 0 or less
    print("It is COLD outside🥶")
    print("Its is CLOUDY☁")
elif temp < 28 and not temp > 0 and is_sunny:
    print("It is WARM outside😎")
    print("Its is CLOUDY☁")


