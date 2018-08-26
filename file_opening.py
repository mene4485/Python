# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, "r")
total = 0
number = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
    	begining = line.find(" ") 
    	number = float(line[begining : begining+7]) 
    	count = count + 1
    	total = total + number


average = total/count

print("Average spam confidence: %s" % average) 



