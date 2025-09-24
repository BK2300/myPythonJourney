import pandas as pd

df = pd.read_csv("pokemonData.csv", index_col="Name") #we pass in a second keyword argument. now names become our first column, so "Name" serves as our index
    # its cool for us who dont remember the nr of the pokemon. But their names

    #selection by column
#print(df["Name"].to_string()) #this returns a single column. But be sure you use upper or lower caps correctly
    #oddly enoug we have to add the "to_string" function after we selected our column
#print(df["Height"].to_string())
#print(df["Weight"].to_string())
#print(df[["Name", "Height", "Weight"]].to_string()) #if we want multiple columns

    # Selection by row/s
#print(df.loc["Pikachu"])
#print(df.loc["Charizard", ["Height", "Weight"]]) #if we only want a specific column/s for a specific pokemon
#print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]]) #shows all the rows between charizard and blastoise

#print(df.iloc[0:11:2, 0:3]) #gives us every second rows, the index of the 10 first pokemons. (remember the last number is exclusive)
# and see only the three first columns


    ## excercise
# we going to still use our first variable we created from before

pokemon = input("Enter a Pokemons name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")

