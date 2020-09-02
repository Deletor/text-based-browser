# create the planets.txt
planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
file = open('planets.txt', 'w', encoding='utf-8')
for item in planet_list:
    file.write(item + '\n')
file.close()
