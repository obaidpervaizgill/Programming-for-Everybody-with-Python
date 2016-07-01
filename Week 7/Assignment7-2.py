fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
    	continue
    line = line.strip() ## removing spaces
    #print line optional
    input = line[line.find("0"):] ##parsing the numeric value
    #print len(input) optional 
    
    num = float(input) ##converting the string into a float
    count = count + 1 ##count is implicitly working on if loop within the loop
    total = total + num
    average = total/count
print "Average spam confidence:",average