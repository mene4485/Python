from random import randrange
B = 0
R = 0
N = 0
for x in range(500):
	a = randrange(1 , 11)
	if a <= 6:
		B += 1
	if a == 7:
		R += 1
	if a >= 8:
		N += 1

print(B/500)
print(R/500)
print(N/500)

