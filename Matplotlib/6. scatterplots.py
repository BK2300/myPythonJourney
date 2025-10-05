# scatter plots = shows the relationshio between two variables
#                 Helps to identify a correlation (+, -, None)
#                 example: study hours vs. test scores

import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) #Hours studied
y1 = np.array([55, 60 ,65, 62, 68, 70, 75, 78, 82, 85, 97]) #grades

x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8])
y2 = np.array([50, 65, 70, 72, 78, 78, 83, 88, 90, 95, 97])

plt.scatter(x1,y1, color="green",
                   alpha=0.5, #Alpha is the transparentcy fo the dots(Not transparentcy removed. itss whats left. so 0.1 is really low!)
                   s = 150, #S is jsut the size of the dots
                   label="Class A")

plt.scatter(x2,y2, color="red",
                   alpha=0.5,
                   s = 150,
                   label="Class B")

plt.title("Test Scores")
plt.xlabel("Hours studied")
plt.ylabel("Grade")

plt.legend() #Legend function is the top left conor, showing whats the meaning of each color means
plt.show()




