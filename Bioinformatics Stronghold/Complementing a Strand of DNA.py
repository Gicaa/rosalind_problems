s = input("DNA: ")

corr = {"A" : "T",
		"T": "A",
		"C": "G",
		"G": "C"}

print("\n")
print("\n")

correspondent = ""

for base in s:
    if base in corr:
        correspondent += corr[base]

fs = correspondent[::-1]

print(fs)
