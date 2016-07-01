fhand = open("mbox.txt")
for line in fhand:
    if line.startswith("From:"):
        print line