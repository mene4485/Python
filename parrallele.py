print ('''Il y deux option:
      -vérifier si (AB) et (CD) sont parallèles 
      -dire les coordonnées d/'un point D tel que (AB) et (CD) soient parallèles ''')
reponse = int ( input ('''Donc quel option tu veux, la une(1) ou la deux(2)
'''))
a = None 
b = None 
if reponse == 1:
	xa = float ( input ('Quel est l`abscisse du point A'))
	ya = float ( input ('Quel est l`ordonnée du point A'))
	xb = float ( input ('Quel est l`abscisse du point B'))
	yb = float ( input ('Quel est l`ordonnée du point B'))
	xc = float ( input ('Quel est l`abscisse du point C'))
	yc = float ( input ('Quel est l`ordonnée du point C'))
	xd = float ( input ('Quel est l`abscisse du point D'))
	yd = float ( input ('Quel est l`ordonnée du point D'))
	a = (yb - ya) / (xb - xa)
    b = (yd - yc) / (xd - xc)
    if a == b:
    	print ('(AB) et (CD) sont parallèles.')
    elif a != b:
    	print ('(AB) et (CD) ne sont pas parallèles.')

