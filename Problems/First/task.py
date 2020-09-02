# read test_file.txt
file = open('test_file.txt', encoding='utf-16')
files = file.readlines()
print(files[0])
file.close()
