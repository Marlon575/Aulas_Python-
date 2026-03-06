Número = int(input("Insira o Número:"))
contador_pares = 0
contador_ímpares = 0
soma_pares= 0
soma_ímpares = 0
for i in range(1,Número + 1):
    contador_pares = (contador_pares + 1)
    soma_pares = (soma_pares + i)
else:
    contador_ímpares = (contador_ímpares + 1)
    soma_ímpares = (soma_ímpares + i)
print(" Quantidade de pares:",contador_pares)
print("Quantidade de ímpares:",contador_ímpares)
print("Soma dos pares:", soma_pares)
print("soma_ímpares:",soma_ímpares)