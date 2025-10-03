#continueing from previous file

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([10, 11, 38, 45])
y3 = np.array([14, 22, 30, 5])

plt.title("Class size", fontsize=25, #We add a title to our plot and increase the font size
                             family="Arial", #what type of writing. arial is probably the most known one
                             fontweight="bold", #we made it bold(fat writing)
                             color="navy")

#now lets set a label for the x-akses
plt.xlabel("Year", fontsize=20,
                         family="Arial",
                         fontweight="bold",
                         color = "cyan")

plt.ylabel("Students", fontsize=20,
                             family="Arial",
                             fontweight="bold",
                             color = "cyan")

plt.tick_params(axis="both", #you can also select a single one. but we seleted both
                color="red")

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

#we can force our plot to only show our values. instead of whats in between
plt.xticks(x) #now it only shows the given years

plt.subplots_adjust(bottom=0.15, #we can adjust the position. meaning this take the bottom and move it upwards. but the top stays
                    left=0.175) #same with left side and shrink it towards right

plt.show()

