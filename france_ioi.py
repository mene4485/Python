nb_page = int(input()) 
page = 2
x = 1
alphabet = []

alphabet3 = []

liste = []

for f in range(ord('a'), ord('z') + 1):
   alphabet.append(chr(f))
for f in range(ord('A'), ord('Z') + 1):
   alphabet3.append(chr(f))
   
for loop in range(nb_page - 1):
   alphabet2 = []
   alphabet4 = []
   x = 1
   message = list(input())
   if page % 2 == 0:
      x = page*3
   elif page % 2 ==1:
       x = (-5)*page
   for je in range(len(alphabet) + 1):
       a = je-x
       if a < 26:
           alphabet2.append(alphabet[a])
       elif a >= 26:
           try:
               alphabet2.append(alphabet[a - 26])
           except:
               alphabet2.append(alphabet[a - 25])
           
   for je in range(len(alphabet3) + 1):
       a = je-x
       if a < 26:
           alphabet4.append(alphabet3[a])
       elif a >= 26:
           try:
               alphabet4.append(alphabet3[a - 26])
           except:
               alphabet4.append(alphabet3[a - 25])
       
   for x in range(len(message)):
       if message[x].islower():
           message[x] = alphabet2[alphabet.index(message[x])]
       elif message[x].isupper():
           message[x] = alphabet4[alphabet3.index(message[x])].upper() 
       else :
           message[x] = message[x]
   page += 1
   liste.append(message)

for x in range(len(liste)):
    print("".join(liste[x])) 
