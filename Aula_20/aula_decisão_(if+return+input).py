def verificar_par(n):
    if n % 2 == 0:
        return "par"
    else:
        return "Impar"
Numero = int(input("Digite o número:"))
resultado =verificar_par(Numero)
print("O número é:",resultado)