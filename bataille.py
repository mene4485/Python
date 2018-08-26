# class Personne:
# 	def __init__(self):
# 		self.nom = 'Dupont'
# 		self.age = '25'
# 		self.prenom = 'Jacques'
# 		self.lieu_residence = 'Toronto'

# class Personne2:
# 	def __init__(self, nom, prenom):
# 		self.nom = nom
# 		self.prenom = prenom
# 		self.age = '25'
# 		self.lieu_residence = 'Montreal'

# # Ajoute un à chaque fois qu'on cree un objet
# class Compteur:
# 	creer = 0
# 	def __init__(self):
# 		Compteur.creer += 1


# class TableauNoir:
# 	def __init__(self):
# 		self.surface=''	
# 	def ecrire(self, message_a_ecrire):
# 		if self.surface != '':
# 			self.surface+='\n'
# 		self.surface += message_a_ecrire
# 	def lire(self):
# 		print(self.surface)
# 	def effacer(self):
# 		self.surface = ''


# class Compteur2:
# 	cree = 0
# 	def __init__(self):
# 		Compteur2.cree += 1
# 	def combien(cls):
# 		print("Jusqu'à présent, {} objets ont été créés.".format(cls.cree))
# 	combien = classmethod(combien)


# class Test:
#     def afficher():
#         print("On affiche la même chose.")
#         print("peu importe les données de l'objet ou de la classe.")
#     afficher = staticmethod(afficher)


# class Personne3:
#     def __init__(self, nom, prenom):
#         self.nom = nom
#         self.prenom = prenom
#         self.age = 33
#         self._lieu_residence = "Paris"
#     def _get_lieu_residence(self):   
#         print("On accède à l'attribut lieu_residence !")
#         return self._lieu_residence
#     def _set_lieu_residence(self, nouvelle_residence):
#         print("Attention, il semble que {} déménage à {}.".format( \
#                 self.prenom, nouvelle_residence))
#         self._lieu_residence = nouvelle_residence
#     lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

a = int(input())
b = int(input())
c = int(input())
if a == 0:

	if b == 0:
		if c == 0:
			print(0)
		else:
			print(0)
	else:
		if c == 0:
			print(1)
		else:
			print(1)

else :

	if b == 0:
		if c == 0:
			print(0)
		else:
			print(1)
	else:
		if c == 0:
			print(1)
		else:
			print(1)

