# mylist = []
# mylist.append(1)
# mylist.append(2)
# mylist.append(3)
# mylist.append(100)

# print(mylist)
# print(len(mylist))
# print(mylist[3])


mylist2 = []
mylist2.append("a")
mylist2.append("b")

print(mylist2)
print(len(mylist2))

mylist2.remove("a")
mylist2.remove("b")

print(mylist2)
print(len(mylist2))

for x in mylist2:
    print("Value: " + str(x))