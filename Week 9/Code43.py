count = dict()
names = ["csev", "cven", "csev", "zqian", "cwen"]
for i in names:
    if i not in count:
        count[i] = 1 ##create a variable and assign 1 to it
    else:
        count[i] = count[i] + 1
print count