#continueing from previous file

import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__) #version 3.10.6

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20]) #student in a class
y2 = np.array([10, 11, 38, 45])
y3 = np.array([14, 22, 30, 5])


    # constantly inputting the marker. color width etc. took way to long time. so we create a dictionary
    # meaning this has become our default and this cant be changed. or else we have to create a new dictonary
line_style = dict(marker=".", #marker sets a custom string to a breaking point on your plot (you can find more online "matplotlib.marker")
                  markersize=20, #"ms" works too.
                  markerfacecolor="red", #You can also use "mfc". But choose between name. RGB value or hexodimal values or HSL values
                  markeredgecolor="red", #this is for the edges around the marker
                  linestyle="solid", #you can also set the style to "None" for no line
                  linewidth=4,
                  color="cyan") #line color)
#Or lets say u want to change color. remove color from above. and insert them seperatly before the dictionary

plt.plot(x, y1, **line_style)

    #what if we cant more line ?
plt.plot(x, y2, **line_style)
plt.plot(x, y3, **line_style)


plt.show()

