count = 0
sum = 0
print "Before",count,sum

for the_num in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + the_num
    print count, sum, the_num

print "After", count, sum, sum/count