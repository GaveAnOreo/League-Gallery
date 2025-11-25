# ALIEN COLORS #2
alien_colors = [{'color': 'green'}, {'color': 'red'}, {'color': 'yellow'}]

for alien in alien_colors:
    if alien['color'] == 'green':
        print("Player just earned 5 points!")
    else:
        print("Player just earned 10 points")
    break

# ALIEN COLORS #2 NO GREEN
alien_colors = [{'color': 'red'}, {'color': 'yellow'}]

for alien in alien_colors:
    if alien['color'] == 'green':
        print("Player just earned 5 points!")
    else:
        print("Player just earned 10 points")
    break
print()