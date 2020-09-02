user = input()
a, b = 0, 0
for i in range(len(user)):
    if i == 'A':
        b += 1
    a += 1
print(round(b / a, 2))
