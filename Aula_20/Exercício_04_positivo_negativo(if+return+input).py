def verificador(n):
    if n > 0:
        return "Número positivo"
    elif n < 0:
        return "Número negativo"
    else:
        return "Zero"
Numero = int(input("Digite um número:"))
resultado = verificador(Numero)
print("O número é:",resultado)