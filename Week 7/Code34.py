fhand = open("mbox.txt")
for line in fhand:
    line = line.strip()
    if line.startswith("From:"): ##new command that is why a colon is required
        print line
        
##for each line in fhand remove spaces and then find a line that starts with our parameter
##then print that particular line