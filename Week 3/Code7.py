astr = "Hello Bob"
try:
	istr = int(astr)
except:
	istr = -1           # if fails this alternate code prints otherwise prints it
print "First",istr

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1
print "Second", istr

astr = "Bob"
try:
    print "Hello"
    istr = int(astr)
    print "There"
except:
    istr = -1
print "Done", istr
 