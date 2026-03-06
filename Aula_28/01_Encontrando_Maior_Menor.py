lista = []
for i in range(5):# Usamos para chamar a variavel `numero` 5 vezes.
    numero = int(input("Digite um número: "))
    lista.append(numero)
print("Números digitados: ", lista)
maior = lista[0]
menor = lista[0]
for numero in lista:
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor < numero
print("Maior número: ",maior)
print("Menor número: ", menor)
