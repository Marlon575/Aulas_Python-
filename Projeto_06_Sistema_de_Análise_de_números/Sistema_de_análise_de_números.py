lista = []
for i in range(5):
    numeros = int(input("Digite o número para análise: "))
    lista.append(numeros)
print("Números analisados: ", lista)
soma = 0
maior = lista[0]
menor = lista[0]

for numero in lista:
    soma += numero#
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero

print("O maior número é: ", maior)
print("O menor número é:", menor)

print("A soma dos números é: ", soma)
media = soma /len(lista)

print("A media dos números é: ", media)
