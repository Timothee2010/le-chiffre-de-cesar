### creer l'index ###

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

### interface personne ###

chaineACrypter = input("S'il te plait, entre un message a crypter :")
chaineACrypter = chaineACrypter.upper()
quantitedecalage = int(input("S'il te plait, entre un nombre entier de 1 a 25 en guise de cle."))
chaineCryptee = ""

### fonctinnoment ###

for caractereActuel in chaineACrypter:
  position = alphabet.find(caracterACctuel)
  nouvelleposition = position + quantitedecalage
  chaineCryptee = chaineCryptee + alphabet[nouvelleposition]
print("ton message crypte est", chaineCryptee)

### ponctuation ###

for caractereActuel in chaineACrypter:
  position = alphabet.find(caractereActuel)
  nouvelleposition = position + quantitedecalage
  if caractereActuel in alphabet:
    chaineCryptee = chaineCryptee + alphabet[nouvelleposition]
  else:
    chaineCryptee = chaineCryptee + caractereActuel
