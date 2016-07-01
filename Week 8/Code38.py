total = 0
count = 0
while True:
    inp = raw_input("Enter a number")
    if inp == "done":
        break
    inp = float(inp)
    total = total + inp
    count = count + 1

average = total/count
print "Average is:", average