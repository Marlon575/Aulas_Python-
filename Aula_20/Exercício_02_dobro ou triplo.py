def Dobro_ou_triplo(n):
    if n >10:
        return n * 3
    else:
        return n * 2
Numero = int(input("Digite o Número:"))
resultado = Dobro_ou_triplo(Numero)
print("Resultado:",resultado)