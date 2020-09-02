# read test.txt
file = open('test.txt')
for i in file.readlines():
    print(i[0])
file.close()
