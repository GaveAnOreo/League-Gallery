# ALIEN COLORS #1
alien_colors = [{'color': 'green'}, {'color': 'red'}, {'color': 'yellow'}]

for alien in alien_colors:
    if alien['color'] == 'green':
        print("Player just earned 5 points!")
        break
# NO OUPUT ALIEN COLORS #1
alien_colors = [{'color': 'red'}, {'color': 'yellow'}]

for alien in alien_colors:
    if alien['color'] == 'green':
        print("Player just earned 5 points!")
        break
print()