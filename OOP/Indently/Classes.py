class Microwave: # classes always have to start with an uppercase
    def __init__(self, brand: str, power_rating: str) -> None:
# __init__ is a dunder method and on default it returns none
        self.brand = brand
        self.power_rating = power_rating
        self.turn_on: bool = False
# self just referes to whatever instants youre currently using.

    def turn_on(self) -> None:
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on")
    else:
        self.turned_on = True
        print(f"Microwave ({self.brand}) is now turned on")


    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave ({self.brand}) is now turned off")
    else:
        self.turned_on = True
        print(f"Microwave ({self.brand}) is already turned off")

    def run(self, seconds: int) -> None:
        if sekf.turned_on:
            print(f"Running ({self.brand} for {seconds} seconds")
        else:
            print(f"A mysterical force whispers:" "Turn on your microwave first")


# Variable (smeg is a brand name).
# First microwave is a type annotation. (it can be safely ignored)
# the second microwave() is a instance of that class
smeg: Microwave = Microwave('Smeg', 'B')


















