def verificar_numero(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"
Valor = verificar_numero(5)
print(Valor)