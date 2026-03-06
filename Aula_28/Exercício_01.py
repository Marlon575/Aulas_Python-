lista = []
for i in range(5):
    Num1 = int(input("Digite os números:"))
    lista.append(Num1)
print("Números digitados:", lista)
maior = lista[0]
menor = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print("Maior número é:",maior)
print("Menor número é:", menor)

