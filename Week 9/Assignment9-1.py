fname = raw_input("Enter file:")
fh = open(fname)
counts = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    
    if len(words) < 1:
        continue
        
    if words[0] != "From":
        continue
    words = words[1]
    #print words
    #for word in words:
    if words in counts:
        counts[words] = counts[words] + 1
    else:
        counts[words] = 1
    #print counts

bigemail = None
bigvalue = None
for email,value in counts.items():
    if value > bigvalue: #I ran if on only one iteration variable
        bigvalue = value
        bigemail = email
print bigemail,bigvalue
        
