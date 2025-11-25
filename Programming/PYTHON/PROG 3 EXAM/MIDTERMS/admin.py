from users import User

class Admin(User):

    def __init__(self, first_name, last_name, age, email, location, privileges):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = privileges

    def show_privileges(self):
        print("\nAdmin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

def main():
    user1 = User("John", "Doe", 28, "john.doe@example.com", "New York")
    user2 = User("Jane", "Smith", 32, "jane.smith@example.com", "London")
    admin = Admin(
        "Super", "Admin", 35, "super.admin@example.com", "Headquarters",
        ["can add post", "can delete post", "can ban user"]
    )

    user1.describe_user()
    user1.greet_user()
    print()

    user2.describe_user()
    user2.greet_user()
    print()

    admin.describe_user()
    admin.show_privileges()

main()