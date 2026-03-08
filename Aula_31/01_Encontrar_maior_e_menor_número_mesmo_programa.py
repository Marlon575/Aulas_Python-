lista = []
for i in range (5):
    numero = int(input("Digite os números: "))
    lista.append(numero)

maior = lista[0]
menor = lista[0]

for numero in lista:
    if numero > maior:# Se encontrar um número da lista, maior que o primeiro número da lista.
        maior = numero # Maior passa a ser esse número encontrado.
    
    if numero < menor: # Se encontrar um número ds lista, menor que o primeiro número da lista.
        menor = numero # Menor passa a ser esse número encontrsdo.

print("Maior número:", maior)
print("Menor número:", menor)