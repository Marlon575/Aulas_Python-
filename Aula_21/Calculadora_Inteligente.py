def Soma(a,b):
    return a + b
def Subtração(a,b):
    return a - b
def Divisão (a,b):
    return a / b
def Multiplicação(a,b):
    return a * b

Num1 = float(input("Digite o primeiro número:"))
Num2 = float(input("Digite o segundo número:"))

print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")

opcao = input("Digite o número da operação: ")

if opcao =="1":
    resultado = Soma(Num1,Num2)
elif opcao == "2":
    resultado = Subtração(Num1,Num2)
elif opcao == "3":
    resultado = Divisão(Num1,Num2)
elif opcao == "4":
    resultado = Multiplicação(Num1,Num2)
else:
    resultado = "Operação inválida"

print("Resultado", resultado)