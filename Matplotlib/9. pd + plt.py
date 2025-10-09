# this is how to use pandas & matplotlib togethers

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("pokemonData.csv")

type_count = df["Type1"].value_counts(ascending=True) #The value function counts the Type1 in cronological order(so 28 water types down to 2 ice types)
#the horizontal barchart is decending on default. So we mad it ascending for reversing it

plt.barh(type_count.index, type_count.values, color="pink",
                                              edgecolor="black")

plt.title("# of pokemon by Primary type")
plt.xlabel("Count")
plt.ylabel("Primary type")
plt.tight_layout()
plt.show()






