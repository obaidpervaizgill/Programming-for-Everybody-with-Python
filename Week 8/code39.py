mylist = list()
while True:
    inp = raw_input("Enter a number:")
    if inp == "done":
        break
    inp = float(inp)
    mylist.append(inp)
    
average = sum(mylist)/len(mylist)
print "Average is:", average