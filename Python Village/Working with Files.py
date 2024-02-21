with open("rosalind_ini5.txt", "r") as file:
    f = file.readlines()
    o = open("output.txt", "w")
    for line in f:
        if (f.index(line) + 1) % 2 == 0:
            o.write(line)
        else:
            pass
