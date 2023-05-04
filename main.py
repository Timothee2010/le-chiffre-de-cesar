### creer l'index ###

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

### interface personne ###

chaineacrypter = input("S'il te plait, entre un message a crypter :")
chaineacrypter = chaineacrypter.upper()
quantitedecalage = int(input("S'il te plait, entre un nombre entier de 1 a 25 en guise de cle."))
chainecryptee = ""

### fonctinnoment ###

for caractereactuel in chaineacrypter:
  position = alphabet.find(caractereactuel)
  nouvelleposition = position + quantitedecalage
  chainecryptee = chainecryptee + alphabet[nouvelleposition]
print("ton message crypte est", chainecryptee)

### ponctuation ###

for caractereactuel in chaineacrypter:
  position = alphabet.find(caractereactuel)
  nouvelleposition = position + quantitedecalage
  chainecryptee = chainecryptee + alphabet[nouvelleposition]
 
