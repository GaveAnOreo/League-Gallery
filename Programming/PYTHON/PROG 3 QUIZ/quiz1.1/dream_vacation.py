poll_results = {}

while True:
    name = input("What is your name? ")
    vacation_place = input("If you could visit one place in the world, where would you go? ")

    poll_results[name] = vacation_place

    continue_poll = input("Would you like to let another person respond? (yes/no): ")
    if continue_poll.lower() == 'no':
        break

print("\n--- Poll Results ---")
for name, place in poll_results.items():
    print(f"{name} would like to visit {place}.")
