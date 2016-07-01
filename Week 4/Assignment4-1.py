def computepay(h,r):
        h=float(h)
        r=float(r)
        if h <= 40:
                return h*r
        if h > 40:
                hb = 40
                ho = h-40
                return hb*r+ho*r*1.5
