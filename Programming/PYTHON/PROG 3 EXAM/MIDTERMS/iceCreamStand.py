from restaurants import Restaurant

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type, location, rating, flavors):
        super().__init__(name, cuisine_type, location, rating)
        self.flavors = flavors

    def display_flavors(self):
        print(f"Available Flavors: {', '.join(self.flavors)}")

def main():
    ice_cream_stand = IceCreamStand(
        "Cool Cones", "Dessert", "Beachfront", 4.8, ["Vanilla", "Chocolate", "Strawberry", "Mint"]
    )
    ice_cream_stand.describe_restaurant()
    ice_cream_stand.display_flavors()

main()