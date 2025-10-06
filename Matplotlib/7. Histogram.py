# Histograms = A visual representations of the distribution of quantitative data.
#              They group values into intervals and counts how many fall in each range.

import numpy as np
import matplotlib.pyplot as plt

# "loc" stands for location. mean where is the median
# "scale" is the standard deviation (spread or width of the histogram if you dont remember)
# "size" is how many number we want to generate (since histograms ise more useful with larger datasets)
scores = np.random.normal(loc=80, scale=10, size=100) #we call the normal function for a normal distribution
scores = np.clip(scores, 0, 100) #This is more for when you use bigger nubmer and dont want outlier(outlier been pulled back to 100 or 0). Her we set a upper limit to 100 and lowest to 0


plt.hist(scores,bins=10, #"bins" is the number of bars(bins) in our histogram
                color="cyan",
                edgecolor="black") #by degault, we dont have any colors and it looks like a big blob
plt.title("Exam Scores")
plt.xlabel("Scores")
plt.ylabel("number of students")

plt.show()


