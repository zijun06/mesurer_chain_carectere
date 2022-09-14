#Entrant:
#Une chaîne de caractère qui contient seulement des mots en minuscules ainsi que des espaces. Peut contenir des mots de la langue française, mais aussi des onomatopées.

#Sortant:
#Vous devez afficher dans la console le nombre de mot exact.

chaine = str(input("Entre le la chane de carectere que vous voulez calculer: "))

def word_count():
  print("vous avez ", len(chaine.split(" ")), "carectere dasn cette chain.")

word_count()
