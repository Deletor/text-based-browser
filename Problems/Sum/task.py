# read sums.txt
file = open('sums.txt')
line = file.readlines()
a = 0
for i in line:
    a = int(i.split()[0]) + int(i.split()[1])
    print(a)
file.close()
