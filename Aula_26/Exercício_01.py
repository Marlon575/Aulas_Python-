Lista = []
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o Segundo número:"))
num3 = int(input("Digite o terceiro número:"))
Lista.append(num1)
Lista.append(num2)
Lista.append(num3)
print("Os Números da lista são:", Lista)
maior =Lista[0]
for numero in  Lista:
    if numero > maior:
        maior = numero
print("O maior Número da lista é:",  maior)
