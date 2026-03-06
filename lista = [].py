lista = []
for i in range(5):
    numeros = int(input("Digite o número para análise: "))
    lista.append(numeros)
print("Números análisados: ", lista)
soma = 0
maior = lista[0]
menor = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero

print("O maior número é: ", maior)
print("O menor número é:", menor)

for numero in lista:
    soma = soma + numero

print("A soma dos númeos é: ", soma)
media = soma /len(lista)

print("A media dos números é: ", media)