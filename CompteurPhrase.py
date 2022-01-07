def comptPhrase(str:str):
    res=str.count('.')
    res+=str.count('!')
    res += str.count('?')
    return res
