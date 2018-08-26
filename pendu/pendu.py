import random
from tkinter import *
import time
tk = Tk()
liste = ["armoire", "boucle", "buisson", "bureau","chaise", "carton","couteau", "fichier", "garage", "glace", "journal", "kiwi", "lampe", "liste", "montagne", "remise", "sandale", "taxi", "vampire", "volant" , "kayak" , "yack" , "zyphir" , "pendu" , "suivant" , "ainsi" , "car" , "methode" , "exception" , "intervalle" , "programme" , "chien" , "chat" , "dauphin" , "lapin" , "cochon" , "compas" , "regle" , "livre" , "marche" , "eau" , "ligne" , "cercle" , "vecteur" , "texte" , "wapiti" , "kangourou" , "chocolat" , "poesie" , "stylo" , "manuel" , "colle" , "calculatrice" , "trousse" , "feuille" , "arbre" , 'angle', 'armoire', 'banc', 'bureau', 'cabinet', 'carreau', 'chaise', 'classe', 'clef', 'coin', 'couloir', 'dossier', 'eau', 'ecole', 'entrer', 'escalier', 'etagere', 'exterieur', 'fenetre', 'interieur', 'lavabo', 'lit', 'marche', 'matelas', 'maternelle', 'meuble', 'mousse', 'mur', 'peluche', 'placard', 'plafond', 'porte', 'poubelle', 'radiateur', 'rampe', 'rideau', 'robinet', 'salle', 'salon', 'serrure', 'serviette', 'siege', 'sieste', 'silence', 'sol', 'sommeil', 'sonnette', 'sortie', 'table', 'tableau', 'tabouret', 'tapis', 'tiroir', 'toilette', 'vitre', 'aller', 'amener', 'apporter', 'appuyer', 'attendre', 'bailler', 'coucher', 'dormir', 'eclairer', 'emmener', 'emporter', 'entrer', 'fermer', 'frapper', 'installer', 'lever', 'ouvrir', 'presser', 'rechauffer', 'rester', 'sonner', 'sortir', 'venir', 'absent', 'assis', 'bas', 'haut', 'present', 'gauche', 'droite', 'debout', 'dedans', 'dehors', 'face', 'loin', 'pres', 'tard', 'tot', 'apres', 'avant', 'contre', 'dans', 'de', 'derriere', 'devant', 'du', 'sous', 'sur', 'crayon', 'stylo', 'feutre', 'mine', 'gomme', 'dessin', 'coloriage', 'rayure', 'peinture', 'pinceau', 'couleur', 'craie', 'papier', 'feuille', 'cahier', 'carnet', 'carton', 'ciseaux', 'decoupage', 'pliage', 'pli', 'colle', 'affaire', 'boite', 'casier', 'caisse', 'trousse', 'cartable', 'jeu', 'jouet', 'pion', 'domino', 'puzzle', 'cube', 'perle', 'chose', 'forme', 'carre', 'rond', 'pate', 'modeler', 'tampon', 'livre', 'histoire', 'bibliotheque', 'image', 'album', 'titre', 'conte', 'dictionnaire', 'magazine', 'catalogue', 'page', 'ligne', 'mot', 'enveloppe', 'etiquette', 'carte', 'appel', 'affiche', 'alphabet', 'appareil', 'camescope', 'cassette', 'chaine', 'chanson', 'chiffre', 'contraire', 'difference', 'doigt', 'ecran', 'ecriture', 'film', 'fois', 'foi', 'idee', 'instrument', 'intrus', 'lettre', 'liste', 'magnetoscope', 'main', 'micro', 'modele', 'musique', 'nom', 'nombre', 'orchestre', 'ordinateur', 'photo', 'point', 'poster', 'pouce', 'prenom', 'question', 'radio', 'sens', 'tambour', 'telecommande', 'telephone', 'television', 'trait', 'trompette', 'voix', 'xylophone', 'zero', 'chanter', 'chercher', 'choisir', 'chuchoter', 'coller', 'colorier', 'commencer', 'comparer', 'compter', 'construire', 'continuer', 'copier', 'couper', 'dechirer', 'decoller', 'decorer', 'decouper', 'demolir', 'dessiner', 'dire', 'discuter', 'ecouter', 'ecrire', 'effacer', 'entendre', 'entourer', 'envoyer', 'faire', 'finir', 'fouiller', 'gouter', 'imiter', 'laisser', 'lire', 'mettre', 'montrer', 'ouvrir', 'parler', 'peindre', 'plier', 'poser', 'prendre', 'preparer', 'ranger', 'reciter', 'recommencer', 'regarder', 'remettre', 'repeter', 'repondre', 'sentir', 'souligner', 'tailler', 'tenir', 'terminer', 'toucher', 'travailler', 'trier', 'ami', 'attention', 'camarade', 'colere', 'copain', 'coquin', 'dame', 'directeur', 'directrice', 'droit', 'effort', 'eleve', 'enfant', 'fatigue', 'faute', 'fille', 'garcon', 'gardien', 'madame', 'maitre', 'maitresse', 'mensonge', 'ordre', 'personne', 'retard', 'joueur', 'sourire', 'travail', 'aider', 'defendre', 'desobeir', 'distribuer', 'echanger', 'expliquer', 'gronder', 'obeir', 'obliger', 'partager', 'preter', 'priver', 'promettre', 'progres', 'progresser', 'punir', 'quitter', 'raconter', 'expliquer', 'refuser', 'separer', 'blond', 'brun', 'calme', 'curieux', 'different', 'doux', 'enerver', 'gentil', 'grand', 'handicape', 'inseparable', 'jaloux', 'moyen', 'muet', 'noir', 'nouveau', 'petit', 'poli', 'propre', 'roux', 'sage', 'sale', 'serieux', 'sourd', 'tranquille', 'arrosoir', 'assiette', 'balle', 'bateau', 'boite', 'bouchon', 'bouteille', 'bulles', 'canard', 'casserole', 'cuillere', 'cuvette', 'douche', 'entonnoir', 'gouttes', 'litre', 'moulin', 'pluie', 'poisson', 'pont', 'pot', 'roue', 'sac', 'plastique', 'saladier', 'seau', 'tablier', 'tasse', 'trous', 'verre', 'agiter', 'amuser', 'arroser', 'attraper', 'avancer', 'baigner', 'barboter', 'boucher', 'bouger', 'deborder', 'doucher', 'eclabousser', 'essuyer', 'envoyer', 'couler', 'partir', 'flotter', 'gonfler', 'inonder', 'jouer', 'laver', 'melanger', 'mouiller', 'nager', 'pleuvoir', 'plonger', 'pousser', 'pouvoir', 'presser', 'recevoir', 'remplir', 'renverser', 'secher', 'serrer', 'souffler', 'tirer', 'tourner', 'tremper', 'verser', 'vider', 'vouloir', 'amusant', 'chaud', 'froid', 'humide', 'interessant', 'mouille', 'sec', 'transparent', 'moitie', 'autant', 'beaucoup', 'encore', 'moins', 'peu', 'plus', 'trop', 'anorak', 'arc', 'bagage', 'baguette', 'barbe', 'bonnet', 'botte', 'bouton', 'bretelle', 'cagoule', 'casque', 'casquette', 'ceinture', 'chapeau', 'chaussette', 'chausson', 'chaussure', 'chemise', 'cigarette', 'col', 'collant', 'couronne', 'cravate', 'culotte', 'echarpe', 'epee', 'fee', 'fleche', 'fusil', 'gant', 'habit', 'jean', 'jupe', 'lacet', 'laine', 'linge', 'lunettes', 'magicien', 'magie', 'maillot', 'manche', 'manteau', 'mouchoir', 'moufle', 'noeud', 'paire', 'pantalon', 'pied', 'poche', 'prince', 'pyjama', 'reine', 'robe', 'roi', 'ruban', 'semelle', 'soldat', 'sociere', 'tache', 'taille', 'talon', 'tissu', 'tricot', 'uniforme', 'valise', 'veste', 'vetement', 'changer', 'chausser', 'couvrir', 'deguiser', 'deshabiller', 'enlever', 'habiller', 'lacer', 'porter', 'ressembler', 'clair', 'court', 'etroit', 'fonce', 'joli', 'large', 'long', 'multicolore', 'nu', 'use', 'bien', 'mal', 'mieux', 'presque', 'aiguille', 'ampoule', 'avion', 'bois', 'bout', 'bricolage', 'bruit', 'cabane', 'carton', 'clou', 'colle', 'crochet', 'elastique', 'ficelle', 'fil', 'marionnette', 'marteau', 'metal', 'metre', 'morceau', 'moteur', 'objet', 'outil', 'peinture', 'pinceau', 'planche', 'platre', 'scie', 'tournevis', 'vis', 'voiture', 'arracher', 'attacher', 'casser', 'coudre', 'detruire', 'ecorcher', 'enfiler', 'enfoncer', 'fabriquer', 'mesurer', 'percer', 'pincer', 'reparer', 'reussir', 'servir', 'taper', 'trouer', 'trouver', 'adroit', 'difficile', 'dur', 'facile', 'lisse', 'maladroit', 'pointu', 'tordu', 'accident', 'aeroport', 'camion', 'engin', 'feu', 'frein', 'fusee', 'garage', 'gare', 'grue', 'helicoptere', 'moto', 'panne', 'parking', 'pilote', 'pneu', 'quai', 'train', 'virage', 'vitesse', 'voyage', 'wagon', 'zigzag', 'arreter', 'atterrir', 'bouder', 'charger', 'conduire', 'demarrer', 'disparaitre', 'donner', 'ecraser', 'envoler', 'garder', 'garer', 'manquer', 'partir', 'poser', 'reculer', 'rouler', 'tendre', 'transporter', 'voler', 'abime', 'ancien', 'blanc', 'bleu', 'casse', 'cinq', 'dernier', 'deux', 'deuxieme', 'dix', 'gris', 'gros', 'huit', 'jaune', 'meme', 'neuf', 'pareil', 'premier', 'quatre', 'rouge', 'sept', 'seul', 'six', 'solide', 'trois', 'troisieme', 'un', 'vert', 'dessus', 'autour', 'vite', 'vers', 'acrobate', 'arret', 'arriere', 'barre', 'barreau', 'bord', 'bras', 'cerceau', 'chaise', 'cheville', 'chute', 'coeur', 'corde', 'corps', 'cote', 'cou', 'coude', 'cuisse', 'danger', 'doigts', 'dos', 'echasses', 'echelle', 'epaule', 'equipe', 'escabeau', 'fesse', 'filet', 'fond', 'genou', 'gymnastique', 'hanche', 'jambe', 'jeu', 'mains', 'milieu', 'montagne', 'mur', 'escalade', 'muscle', 'numero', 'ongle', 'parcours', 'pas', 'passerelle', 'pente', 'peur', 'pied', 'plongeoir', 'poignet', 'poing', 'pont', 'signe', 'singe', 'poutre', 'equilibre', 'prise', 'riviere', 'crocodile', 'roulade', 'pirouette', 'saut', 'serpent', 'sport', 'suivant', 'tete', 'toboggan', 'tour', 'trampoline', 'tunnel', 'ventre', 'accrocher', 'appuyer', 'arriver', 'baisser', 'balancer', 'bondir', 'bousculer', 'cogner', 'courir', 'danser', 'depasser', 'descendre', 'ecarter', 'escalader', 'gagner', 'gener', 'glisser', 'grimper', 'marcher', 'pattes', 'debout', 'monter', 'montrer', 'pencher', 'percher', 'perdre', 'ramper', 'rater', 'remplacer', 'respirer', 'retourner', 'revenir', 'sauter', 'soulever', 'suivre', 'tomber', 'transpirer', 'traverser', 'dangeureux', 'epais', 'fort', 'groupe', 'immobile', 'rond', 'serre', 'souple', 'ensemble', 'ici', 'jamais', 'toujours', 'souvent', 'bagarre', 'balancoire', 'ballon', 'bande', 'bicyclette', 'bille', 'cage', 'ecureuil', 'cerf', 'volant', 'chateau', 'coup', 'cour', 'course', 'echasse', 'flaque', 'eau', 'paix', 'pardon', 'partie', 'pedale', 'pelle', 'pompe', 'preau', 'raquette', 'rayon', 'recreation', 'sable', 'sifflet', 'signe', 'tas', 'tricycle', 'tuyau', 'velo', 'file', 'rang', 'bagarrer', 'battre', 'cacher', 'cracher', 'creuser', 'crier', 'degonfler', 'dispute', 'empecher', 'galoper', 'hurler', 'jongler', 'lancer', 'pedaler', 'plaindre', 'pleurer', 'poursuivre', 'proteger', 'saigner', 'salir', 'siffler', 'surveiller', 'trainer', 'trouver', 'fou', 'mechant' , "kilo" ]


def fa(coup):
	if coup == 7:
		canvas.create_line(50,245,300,245)
		canvas.create_line(125,245,125,50)
	if coup == 6:
		canvas.create_line(125,50,225,50)
		canvas.create_line(225,50,225,70)
	if coup == 5:
		canvas.create_oval(205 , 70 , 245, 110 , fill = 'pink')
	if coup == 4:
		canvas.create_line(225 , 110 , 225, 175)
	if coup == 3:
		canvas.create_line(225 , 120 , 175, 105)
	if coup == 2:
		canvas.create_line(225 , 120 , 275, 105)
	if coup == 1:
		canvas.create_line(225 , 175 , 190, 200)
	if coup == 0:
		canvas.create_line(225 , 175 , 260, 200)
		canvas.create_text(200 , 25 , text=("Pendu! Le mot est {}.".format(mot))  , font=('Nunito', 30))
		

canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()
coup = 8
lieu_al = random.randrange(0 , len(liste))
mot = liste[lieu_al]
mot_masque = []
reussi = False
for x in mot:
	mot_masque.append("_")
faux = []
o = canvas.create_text(175 , 300 , text=mot_masque , 
	font=('Times', 24))
q = canvas.create_text(10 , 100 , text=faux , 
	font=('Times', 24))
print()
while coup > 0:
	lettre = input("Votre lettre est: ")
	while True:
		if len(lettre) > 1 or lettre==" " :
			lettre = input("Veuillez ressaisir votre lettre: ")
		elif lettre in mot_masque or lettre in faux:
			lettre = input("Vous avez déjà ecrit cette lettre. Veuillez ressaisir votre lettre: ")
		elif lettre.isalpha() == False:
			lettre = input("Vous devez écrire une lettre. Veuillez ressaisir votre lettre: ")
		else:
			break
	re = None
	for x in range(len(mot)):
		if lettre == mot[x]:
			mot_masque[x] = lettre
			re = True
	
	if re == None:
		faux.append(lettre)
		canvas.delete(q)
		q = canvas.create_text(175 , 350 , text=faux , font=('Lobster', 24))
		coup -= 1
		fa(coup)

	canvas.delete(o)
	o = canvas.create_text(175 , 300 , text=mot_masque , font=('Times', 24))
		
	if "".join(mot_masque) == mot:
		canvas.create_text(200 , 20 , text="Bravo!" , font=('Nunito', 40))
		break

tk.mainloop() 