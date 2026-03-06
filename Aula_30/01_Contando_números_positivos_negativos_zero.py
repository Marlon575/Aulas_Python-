lista = [] # Criamos uma lista vazia
for i in range (5): # O programa vai repetir 5 vezes
    numero = int(input("Digite os números: "))
    lista.append(numero) # Guardar os valores da variavel numero

contador_positivo = 0
contador_negativo = 0
contador_zero = 0

for numero in lista: # O programa vai olhar
    if numero > 0:
        contador_positivo +=1

    elif numero < 0:
        contador_negativo +=1

    else:
        contador_zero +=1
print("A quantidade de números positivos são: ",contador_positivo)
print("A quantidade de números negativos são: ", contador_negativo)
print("A quantidade de números zeros é: ", contador_zero)