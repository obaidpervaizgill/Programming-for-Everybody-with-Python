def computepay(h,r):
        h=float(h)
        r=float(r)
        if h <= 40:
                return h*r
        if h > 40:
                hb = 40
                ho = h-40
                return hb*r+ho*r*1.5

h = raw_input("Enter Hours:")
r = raw_input("Rate per Hour:")
p = computepay(h,r)
print p