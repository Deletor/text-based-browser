user = input()
user = user.lower()
user = user.replace('!', '')
user = user.replace('?', '')
user = user.replace('.', '')
user = user.replace(',', '')
print(user)