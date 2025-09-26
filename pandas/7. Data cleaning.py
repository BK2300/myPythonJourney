# Data cleaniing = the process of ficing/removing:
#                  incomplete, incorrect, or irrelevant data.
#                  ~75% of work done with pandas is data cleaning

import pandas as pd

df = pd.read_csv("pokemonData.csv")

    #1. Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])

    #2. Handling missing data (here only 67 pokemons had a second type, so the rest is missing)
# df = df.dropna(subset=["Type2"]) #So now we removed rows of pokemons without a second type or said "NaN" in second type.
df = df.fillna({"Type2": "None"}) #Here we ask to fill all the NaN values to replace them with none, instead of removing them

    #3. Fix inconsisten values
df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                   "Fire": "FIRE",
                                   "Water": "WATER"}) #Just jsut replace their types to be something else. But i only wanted to replace them with the same type, but uppercase

    #4. Standardize text
df["Name"] = df["Name"].str.lower() #Where we made all the characters names lowercase

    #5. Fix data types
df["Legendary"] = df["Legendary"].astype(bool)

    #6. remove duplicate values
df = df.drop_duplicates()

print(df.to_string())





