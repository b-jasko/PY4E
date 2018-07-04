fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    x = line.split()
    for piece in x:
        if piece not in lst:
            lst.append(piece)
lst.sort()
print(lst)
