def make_sandwich(*items):
    print("You ordered a sandwich with the following ingredients:")
    for item in items:
        print(f"- {item}")

make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "tomato")
make_sandwich("peanut butter", "jelly", "banana")
