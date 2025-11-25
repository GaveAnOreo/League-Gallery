class User:

    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print("\nUser Profile:")
        print(f"- Name: {self.first_name} {self.last_name}")
        print(f"- Age: {self.age}")
        print(f"- Email: {self.email}")
        print(f"- Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")


def main():
    user1 = User("John", "Doe", 28, "john.doe@example.com", "New York")
    user2 = User("Jane", "Smith", 32, "jane.smith@example.com", "London")
    user3 = User("Alice", "Johnson", 30, "alice.johnson@example.com", "Toronto")

    user1.describe_user()
    user1.greet_user()
    print()

    user2.describe_user()
    user2.greet_user()
    print()

    user3.describe_user()
    user3.greet_user()

if __name__ == "__main__":
    main()