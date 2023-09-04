w = str(input("Enter word: "))
l = len(w)
f = w[0]
f = f.lower()
w = w[1:l]
w = w + f + "ay"
print(w)
