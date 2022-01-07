def strToArray(str : str,seperator :str):
    tabSeparator = seperator.split(" ")
    temp = str.split()
    for i in tabSeparator:
        temp = temp.split(i)
    return temp

def nbMots(tab):
    return len(tab)