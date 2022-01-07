import re

def strToArray(str : str,seperator):
    return re.split(seperator,str)

def nbMots(tab):
    return len(tab)