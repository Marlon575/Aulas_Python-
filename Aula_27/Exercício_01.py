lista = []
num1 = int(input("Digite o 1ª Número: "))
num2 = int(input("Digite o 2ª Número: "))
num3 = int(input("Digite o 3ª Número: "))
num4 = int(input("Digite o 4ª Número: "))
num5 = int(input("Digite o 5ª Número: "))
lista.append(num1)
lista.append(num2)
lista.append(num3)
lista.append(num4)
lista.append(num5)
print("Os números da lista são: ",lista)
menor = lista [0]
for numero in lista:
    if numero < menor:
        menor = numero
print("O menor númeror da lista: ",menor)