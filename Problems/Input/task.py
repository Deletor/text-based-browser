# write the code here
user = input()
file = open('input.txt', 'w', encoding='utf-8')
file.write(user)
file.close()
