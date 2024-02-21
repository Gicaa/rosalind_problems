txt = input("Input: ")

a = 0
c = 0
g = 0
t = 0

for l in txt.upper():
	if l == "A":
		a += 1

	elif l == "C":
		c += 1

	elif l == "G":
		g += 1

	elif l == "T":
		t += 1

print(f"{a} {c} {g} {t}")
