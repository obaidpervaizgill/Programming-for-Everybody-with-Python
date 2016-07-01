fname = raw_input("Enter file name: ")
fh = open(fname) #opened files
lst = list()
for line in fh: #read it by line
    line = line.rstrip() #white space is reduced for each line
    words = line.split() #line is split into a list of words
    #print "###", words
    for i in words: 
        if i in lst:
            continue
        else:
            lst.append(i)
    lst.sort()
print lst   
    
  
        
