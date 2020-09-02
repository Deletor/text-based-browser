user = input()
num = input()
a = 0
text = ''
for i in user.split(' '):
    a += 1
    if i == num:
        text = text + ' ' + str(a - 1)
if text == '':
    text = 'not found'
print(text)
