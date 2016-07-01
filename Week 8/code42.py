fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    #print "+++++++++++++", line
    #if line == " " : continue ###another kind of guardian pattern
    words = line.split()
    #print words
    if words == []: ###guardian pattern for a blank list
    #if len(words) < 1 : continue ###another kind of guardian pattern
        continue
    if words[0] != "From":
        continue
    print "==============", words[2]