
# for i in range(5):
#     if i == 3:
#         break
#     print(i)

text = input()

while True:
    if text == "stop" or text == "end":
        print("Program has stopped.")
        break
    print("text: {}".format(text))
    text = input()