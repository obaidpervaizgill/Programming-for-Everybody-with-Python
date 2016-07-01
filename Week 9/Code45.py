counts = dict()
line = raw_input("Enter a line of text:")

words = line.split() #the split takes a string and produces a list
print "Words:", words

print "Counting..."
for i in words:
	counts[i] = counts.get(i,0) + 1 #either create a key or add to it

print"Counts", counts
