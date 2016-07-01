scr = raw_input("Enter Your Score:")
rawscr = float(scr)
if rawscr > 100:
        print "Out of Range"
elif rawscr >= 90:
	print "A"
elif rawscr >= 80:
	print "B"
elif rawscr >= 70:
	print "C"
elif rawscr >= 60:
	print "D"
else:
	print "F"

