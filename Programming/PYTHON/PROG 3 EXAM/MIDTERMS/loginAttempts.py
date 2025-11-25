from users import User

class UserWithLogin(User):

    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

def main():
    user = UserWithLogin("Alice", "Wonderland", 25, "alice.wonderland@example.com", "Paris")

    user.increment_login_attempts()
    user.increment_login_attempts()
    user.increment_login_attempts()
    print(f"Login attempts: {user.login_attempts}")

    user.reset_login_attempts()
    print(f"Login attempts after reset: {user.login_attempts}")

main()