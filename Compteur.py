import CompteurMot
import Recurrence
import CompteurPhrase



message=input("Rentrez votre flux: "  )
liste=input("Rentrez la liste des mots séparé par un espace dont vous souhaitez voir l'occurence :" )



Recurrence.rec(message,liste)
print("il y a "+str(CompteurMot.nbMots(message))+" mot.s")
print("il y a "+str(CompteurPhrase.comptPhrase(message))+" phrases")


