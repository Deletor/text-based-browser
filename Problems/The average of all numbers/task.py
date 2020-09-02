# put your python code here
a = 0
b = 0
c = 0
d = 0
a = input()
b = int(input())
e = b + 1
for i in range(int(a), int(e)):
    if i % 3 == 0:
        c += i
        d += 1
print(c / d)