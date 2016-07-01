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
    words = words[5]  
    hours = words.split(":")
    hours = hours[0]
    #print hours
    if hours in counts:
        counts[hours] = counts[hours] + 1
    else:
        counts[hours] = 1
    #print counts

lst = list()
for key,val in counts.items():
    lst.append((key,val))

lst.sort()

for key,val in lst:
    print key,val
