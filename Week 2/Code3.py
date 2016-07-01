x = 5
if x > 2:
	print"Bigger than 2" # two statements that are part of the if statement
	print"still bigger"
print "Done with 2"

for i in range(5):
	print i
	if i > 2:			# this is a block inside of a block
		print "Bigger than 2"
	print "DOne with i", i
	
y = 42
if y > 1:
	print "More than 1"
	if y < 100:
		print "Less than 100"
		
print "All done"
	
