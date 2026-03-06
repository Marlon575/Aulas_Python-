Numero = int(input("Digite um Número:"))
soma = 0
for i in range (1, Numero + 1):
    if i % 2 == 0:
        soma = soma + i

print("O tolal da soma dos número pares é :", soma)