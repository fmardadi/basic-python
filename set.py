my_set = {"apel", "mangga", "jeruk"}

print(my_set)
print(type(my_set))

for x in my_set:
    print(x)

print("apel" in my_set)
print("melon" in my_set)
print("jeruk" in my_set)

my_set.add("melon")
print(my_set)

my_set.remove("melon")
print(my_set)