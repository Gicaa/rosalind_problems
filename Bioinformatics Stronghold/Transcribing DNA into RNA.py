t = input("DNA: ")
print("\n")
f = ""

for letter in t:
    if letter == "T":
        f += "U"
    else:
        f += letter

print(f)
