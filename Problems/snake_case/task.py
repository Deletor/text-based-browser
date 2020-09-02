a = ''
user = input()
for char in user:
    if char.isupper():
        b = '_'
        char = b + char.lower()
    a += char
print(a)