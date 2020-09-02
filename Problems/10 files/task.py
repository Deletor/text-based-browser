# write your code here
n = 10
a = 0
name = ''
for i in range(n):
    a = i + 1
    name = 'file' + str(a) + '.txt'
    with open(name, 'w') as f:
        f.write(str(a))
