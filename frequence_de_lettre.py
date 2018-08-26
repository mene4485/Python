import sys
import time

text = sys.stdin.readline().upper()  
count = {} 

words = list("".join(text.split())) 

for x in words:
	count[x] = count.get(x , 0) + 1

bigcount = None
bigword = None
for word , c in count.items() :
	if bigcount == None or c > bigcount:
		bigcount = c
		bigword = word

print(bigword) 
