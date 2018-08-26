# file = open("lol.txt")
# count = 0 

# for l in file:
#     count = count + 1

# print("Line Count :", count)

fh = open("sample.txt","r")
nb_de_lettre = 0
nb_de_lettre2 = 0

count = 0
letter1 = 0
for line in fh:
    letter1 = 0
    lettre2 = 0
    print(line.strip())
    for letter in line:
        letter1 += 1
        if letter == " ":
            letter1 -= 1
    for lettre in line:
    	lettre2 += 1
    letter1 = letter1 - 1
    lettre2 = lettre2 - 1
    print("--> %s letters, sans les espaces" % letter1)
    print("--> %s letters, avec les espaces" % lettre2)

    count = count + 1
    nb_de_lettre = nb_de_lettre + letter1
    nb_de_lettre2 = nb_de_lettre2 + lettre2


print(count,"Lines", "and %s letters sans les espaces et %s avec les espaces" % (nb_de_lettre,nb_de_lettre2)) 


