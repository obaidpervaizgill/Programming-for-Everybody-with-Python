counts = dict()
names = ["csev", "cven", "csev", "zqian", "cwen"]
for i in names:
    counts[i] = counts.get(i,0) + 1 ##will either create an entry or update it by adding 1 to it
print counts