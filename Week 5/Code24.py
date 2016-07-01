smallest = None
print "Before"
for the_num in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = the_num
    elif the_num < smallest:
        smallest = the_num
    print smallest, the_num

print "After", smallest

##is is best used for None and False the only reason why we dont use == is 
##because it will try to convert values