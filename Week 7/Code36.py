fhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    if not "@uct.ac.za" in line: ##if this string is not in line them i am continuing
        continue
    print line