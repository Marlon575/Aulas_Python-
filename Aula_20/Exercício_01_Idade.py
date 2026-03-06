def Verificação(Idada):
    if Idada <=17:
        return "Voce e criança"
    elif Idada <=49:
        return "Voce e adulto"
    else:
        return "voce e velho"
Numero =  Verificação(40)
print(Numero)