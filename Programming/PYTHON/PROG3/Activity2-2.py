# POLLING
favorite_languages = {
    'andrea': 'python',
    'benedict': 'ava',
    'paul': 'javascript'
}

people = ['andrea', 'dale', 'paul', 'zakeesha']

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, please take the favorite languages poll.")


# PETS
pets = [
    {'type': 'dog', 'owner': 'benedict'},
    {'type': 'cat', 'owner': 'andrea'},
    {'type': 'rabbit', 'owner': 'paul'}
]

for pet in pets:
    print(f"\nPet Type: {pet['type'].title()}")
    print(f"Owner: {pet['owner'].title()}")


# FAVORITE PLACES
favorite_places = {
    'benedict': ['basketball court', 'coffee shop', 'beach'],
    'dale': ['mall', 'cinema'],
    'james': ['library', 'park', 'mountains']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")
