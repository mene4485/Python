#Ce programme calcule une moyenne

number = list() 

while True:
	try:
		inp = input("Enter a number : ")
		if inp == "done":
			break
		value = float(inp)
		number.append(value)
	except:
		print("Invalid syntax")
	

average = sum(number)/len(number)
print ("Average : ", average)