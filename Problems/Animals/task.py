new_file = open('animals_new.txt', 'w', encoding='utf-8')
a, d = '', ''
b = 0
with open('animals.txt') as f:
    a = f.read().splitlines()
for i in a:
    b += 1
    c = b - 1
    d = d + i + ' '

new_file.write(d)
new_file.close()
