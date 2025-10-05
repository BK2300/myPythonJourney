# pie chart= Circular chart divded into slices to show percentages of the total.
#            Good for cisualizing distribution among categories.

import numpy as np
import matplotlib.pyplot as plt

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 250, 275, 225]) #Its not so benefitial for such a small dataset to use numpy. But we just getting into the habit
colors = ["red", "cyan", "yellow", "green"] #the colors have to be in order of your categories

plt.pie(values, labels=categories,
                autopct="%1.1f%%", #Autoprocentage" sets the procentages of distribution for our pie. procentages have to many decimals. So we write "x.1", meaning only one decimal
                                      #The double percent signs %% meaning with want a percentage sign behind our numbers
                colors=colors,
                explode=[0,0,0,.125], #explode meaning with sort of pulling it out from our pie chart individually(thats why we have the same amount of values af our categories)
                shadow=True, #meaning we make 3d. but its not recommendet for data virsualization
                startangle=93) #If we want it to rotate(positiv number turns it to the left side. While negativ # turns it to the right side)(Smart to have the biggest/most important value be on top right side)

plt.title("Baki's comedy school")

plt.show()

