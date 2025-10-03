# bar chart = compare categories of data by representing each ccategory with a bar

import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruits", "Veggie", "Protein", "Diary", "Sweets"])
values = np.array([4, 3, 2, 5, 3, 1])

plt.bar(categories, values, color="skyblue") #to form the bar chart. categories is on the x-akses, values is y-akses
# To creat a hizzontal bar chart. Use the "barh()" function. (like the one above. jsut with a "h" appended


plt.title("Daily consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()






