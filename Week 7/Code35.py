fhand = open("mbox.txt")
for line in fhand:
    line = line.strip()
    ## skip lines that we are not interested in
    if not line.startswith("From:"):
        continue
    ## include lines that we are interested in
    print line