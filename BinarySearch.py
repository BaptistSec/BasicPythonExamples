words = []

while True:
    element = input("What would you like to add? ")
    if element == "":
        break
    words.append(element)
length = int(len(words))
target = input("What word would you like to look for? ")
middle_position = length // 2
words = sorted(words)
middle = words[middle_position]
while middle != target:
    middle = words[middle_position]
    if target > middle:
        middle_position += 1
        print(middle)
    else:
        print(middle)
        middle_position -= 1




