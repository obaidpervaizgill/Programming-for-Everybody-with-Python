fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    email = words[1]
    address = email.split("@")
    print address[1]