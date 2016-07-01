while True:  ###these loops are indefinite loops
  line = raw_input(">")
  if line[0] == "#":
    continue 
  if line == "done":
    break
  print line
print "Done!"


## continue basically gets back to the start of the loop
