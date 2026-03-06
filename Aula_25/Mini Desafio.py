Numeros = []
Num1 =float(input("Digite o Primeiro Número:"))
Num2 =float(input("Digite o Segundo Número:"))
Num3 =float(input("Digite o Terceiro Número:"))
Numeros.append(Num1)
Numeros.append(Num2)
Numeros.append(Num3)
print(Numeros)
soma = 0
for Numero in Numeros:
    soma = soma + Numero
print("A soma dos Números é igual: ",soma)
Media = soma / len(Numeros)
print("Media igual: ",Media)