# Dictionary = a collectionsof {key:value} pairs
#              ordered and changeable. No duplicates
from matplotlib.typing import CapStyleType

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

    #If you want to see the difference attributes and methods of a dictionary, use the dir-function:
    # (But you can also use help  function, which is more in depth
#print(dir(capitals))

#the capital associated with our contries from our list
if capitals.get("Japan"): # play around with some countries
    print("That capitals exists")
else:
    print("That capital doesnt exist")

# capitals.update({"Germany": "Berlin"}) #updating by adding another value
# capitals.update({"USA": "Los Angeles"}) #And lets change a capital of a country
# capitals.pop("China") #To remove a key value pair, we use the pop method
# capitals.popitem() #We havent indicated where to remove. So its jsut removes the lasts key value pair
# capitals.clear() #clear will clear the entire dictinary

keys = capitals.keys() #keys method will return all of our key within our dictionary

    #keys method
for key in capitals.keys():
    print(key)

    # values method
values = capitals.values()
for value in capitals.values():
    print(value)

    #items method
#items will return a distionary of objects which resembles a 2D lsit of tuples "[(), (), ()]"
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")