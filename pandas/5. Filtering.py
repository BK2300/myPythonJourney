# Filtering = keeping the rows that match a condition

import pandas as pd

df = pd.read_csv("pokemonData.csv")

    # Let us filter out all the pokemons, that is 2meters or above

# tall_pokemon = df[df["Height"] >= 2] #we access our dataframe is a subscript operator
# heavy_pokemon = df[df["Weight"] > 100]
# legendary_pokemon = df[df["Legendary"] == 1] #The boolean value for 1 is "True", so we could also write true instead of 1
#water_pokemon = df[(df["Type1"] == "Water")|
#                  (df["Type2"] == "Water")] #This scrip searches for water pokemon as first or second type. We used the logical "or / |" operator
ff_pokemon = df[(df["Type1"] == "Fire" ) &
                (df["Type2"] == "Flying")] #"This is a "and" operator. we need both conditions to be filled out




print(ff_pokemon)




