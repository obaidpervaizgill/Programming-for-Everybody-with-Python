name = raw_input("Enter file:")
handle = open(name)
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1 #we set the # to 0 so adding will give 1
    #if word in counts:
        #counts[word] = counts[word] + 1
    #else:
        #counts[word] = 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword,bigcount