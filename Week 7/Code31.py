fhand = open("mbox.txt")
count = 0 ##start off with this value
for i in fhand: ##here i will automatically be considered a line
    count = count + 1 ##restore the count as count and 1
print count 