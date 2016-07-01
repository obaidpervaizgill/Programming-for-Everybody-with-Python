data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:12:16 2008"
atpos = data.find("@")
print atpos

spos = data.find(" ", atpos) ##use atpos as a reference and find space
print spos

domain = data[atpos + 1 : spos]
print domain
