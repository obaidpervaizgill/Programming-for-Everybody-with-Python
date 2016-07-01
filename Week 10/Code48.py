fhand = open("romeo.txt")
counts = dict()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
            
lst = list()
for key,val in counts.items():
    lst.append((val,key))
    
lst.sort(reverse=True)

for val,key in lst [:10]:
    print key,val