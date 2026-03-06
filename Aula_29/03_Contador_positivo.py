lista = []
for i in range(5):
    numero = int(input("Digite os números: "))
    lista.append(numero)

contador_positivo = 0

for numero in lista:
    if numero > 0:
        contador_positivo +=1
print("Quantidade de números positivos é: ", contador_positivo)