Numero = int(input("Digite o número:"))
soma = 0
for i in range(1, Numero + 1):
    if i % 2 != 0:
        soma = soma + i
print("O total da soma dos números ímpares é:",soma)