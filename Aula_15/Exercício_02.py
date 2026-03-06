Numero = int(input("Digite o número:"))
soma_pares= 0
soma_Impares = 0
for i in range(1, Numero + 1):
    if i % 2 == 0:
        soma_pares = soma_pares + i
    else:
        soma_ímpares = soma_Impares + i
print("A soma dos número pares é:", soma_pares)
print("A soma dos números ímpares é:", soma_Impares)
