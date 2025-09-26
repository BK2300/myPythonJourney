# aggregate function = Reduces a set of values into a single summary value. Used to summarize and analyse data
#                      Often used with the groupby() function
#                      More specificly the "mean, max, min, sum" etc.



import pandas as pd

df = pd.read_csv("pokemonData.csv")

#(Whole dataframe)
    #You cant find the mean of anything thats not numeric, so youll get a error msg
# print(df.mean(numeric_only=True)) #But with this argument. We print the mean of all the numeric columns and ignore does thats not numeric
# print(df.sum(numeric_only=True)) #The sum of all numeric columns
# print(df.min(numeric_only=True)) #minimum value of all numeric columns
# print(df.max(numeric_only=True)) #maximum value of all numeric columns
# print(df.count()) #counting the values of each column


#(Single column)
# print(df["Height"].mean()) #The mean of "height" column
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())


# What if we "group by" their primary type?
group = df.groupby("Type1")

print(group["Height"].mean()) #So here we found the average Height of all the pokemons, groupped in their fimilar type. (And the result is that, dragon types are on average taller then the rest of them, with a count of 2,66m)
print(group["Height"].sum()) #seems like water type has the greatest high
print(group["Height"].min()) #seems like ground has the smallest member
print(group["Height"].max()) #rock has the one tallest member
print(group["Height"].count()) #Water type as a count of 28 pokemons combined

