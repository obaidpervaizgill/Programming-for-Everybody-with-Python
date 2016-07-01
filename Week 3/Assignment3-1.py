hrs = raw_input("Enter Hours:")
h = float(hrs)
rph = raw_input("Rate per Hour:")
r = float(rph)
if h <= 40:
	print h*r
if h > 40:
        hb = 40
        ho = h-40
        print hb*r+ho*r*1.5
print "total pay"
