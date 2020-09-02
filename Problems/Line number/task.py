# read sample.txt and print the number of lines
file = open('sample.txt')
a = 0
for i in file:
    a += 1
print(a)
file.close()
