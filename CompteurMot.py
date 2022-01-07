import re

def strToArray(str : str,seperator):
    return re.split(seperator,str)

def nbMots(str:str):
    tab = strToArray(str," |\. |\! |\? |\; |\, |\:")
    return len(tab)