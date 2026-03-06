Numero = int(input("Insira o número:"))
contador = 0
for i in range(1, Numero + 1):
    if i % 2 == 0:
        contador = contador + 1
print("Quantidade de Número pares:",contador)