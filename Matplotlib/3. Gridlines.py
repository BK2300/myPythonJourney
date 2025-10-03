# grid() = Helps male plots easier to read by adding reference lines.
#          For better readability

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.grid(axis="y", #it gives rektangles on default. But I think the horizontals only are cooler
         linewidth=3,
         color="orange",
         linestyle="dashdot")

plt.plot(x, y)
plt.show()




