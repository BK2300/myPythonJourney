# Figure = The entire canvas
#Ax = A single plot(Subplot)
    # we dont have to use plots. we can use bars instead also

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])

figure, axes = plt.subplots(2, 2)

axes[0,0].plot(x, x*2, color="red") #here we specify what Axes we wanted to access. So row 0. column 0
axes[0,0].set_title("x*2")

#top right Axes
axes[0,1].bar(x, x**2, color="Blue")
axes[0,1].set_title("x**2")

#bottom left
axes[1,0].hist(x, x**3, color="Green")
axes[1,0].set_title("x**3")

#bottom right
axes[1,1].plot(x, x**4, color="Orange")
axes[1,1].set_title("x**4")

plt.tight_layout() #tight() layout function fixesd the overlapping of the titles on top of the different axes
plt.show()

