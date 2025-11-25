class Restaurant:

    def __init__(self, name, cuisine_type, location, rating):
        self.name = name
        self.cuisine_type = cuisine_type
        self.location = location
        self.rating = rating

    def describe_restaurant(self):
        print(f"Restaurant: {self.name}")
        print(f"Type of Cuisine: {self.cuisine_type}")
        print(f"Location: {self.location}")
        print(f"Rating: {self.rating}/5 stars")

    def open_restaurant(self):
        print(f"The restaurant '{self.name}' is now open!")

def main():
    restaurant = Restaurant("Cafe Delight", "Italian", "Downtown", 4.5)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

main()