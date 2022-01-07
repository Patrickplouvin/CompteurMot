from CompteurMot import strToArray
import CompteurMot



def recurrence(message):
    tab=strToArray(message," ")
    print(tab.count("."))
    
    print(tab)
    
        
recurrence('coucou la tiktokerie.')