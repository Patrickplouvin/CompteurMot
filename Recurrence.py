import CompteurMot

def rec(message,liste):
    occ=[]
    liste=CompteurMot.strToArray(liste," ")
    message=CompteurMot.strToArray(message," |\. |\! |\? |\; |\, |\: ")
    for i in liste:
        print("le mot "+i+" est "+str(message.count(i))+" fois")

