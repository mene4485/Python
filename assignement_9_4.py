fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname , "r")
count = {} 
liste = []

for line in fh:
    if line.startswith("From "):
        words = line.split()
        liste.append(words[1])


for x in liste:
	count[x] = count.get(x , 0) + 1

bigcount = None
bigword = None
for word , c in count.items() :
	if bigcount == None or c > bigcount:
		bigcount = c
		bigword = word

print(bigword, bigcount)



# fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"

# fh = open(fname , "r")
# count = {} 
# lol = 0

# for line in fh:
#     if line.startswith("From "):
#         words = line.split()
#         count[lol] = words[1]
#         lol += 1

# bigcount = None
# bigword = None
# for word , c in count.items() :
# 	if bigcount == None or c > bigcount:
# 		bigcount = c
# 		bigword = word

# print(bigword, bigcount)