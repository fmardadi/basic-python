# read file
f = open("hello.txt", "r")

# read all text
# print(f.read())

# read part of file
# print(f.read(5))

# read line
temp = f.readlines()
print(temp)

for i in range(3):
    a = f.readline()
    if i == 1:
        print(a)
# print(f.readline())
# print(f.readline())
# print(f.readline())

f.close()