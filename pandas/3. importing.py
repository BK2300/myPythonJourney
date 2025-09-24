import pandas as pd

    # finding CSV files:
#df = pd.read_csv("pokemonData.csv")

#print(df) #the data is truncated. meaning we only see the first 5 rows and the last 5 rows
#print(df.to_string()) #to_string will print everything(luckily this dataset isnt that big)


    # finding JSON files:

df = pd.read_json("PokemonData.json")

print(df_string()) 