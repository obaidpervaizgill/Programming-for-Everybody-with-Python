count = 0
total = 0

while True:
    inp = raw_input("Enter a number: ")
   
    #Handle the edge cases
    if inp == "done":
        break
    if len(inp) < 1:
        break ##empty line check done is not good

    #Do the work
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
    count = count + 1
    total = total + num
    print num, total, count

print "Average:", total/count
    