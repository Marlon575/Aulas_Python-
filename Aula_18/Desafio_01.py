def calculadora(a,b):
    resultado_soma = a + b
    resultado_subtração = a - b 
    resultado_multiplicação = a * b
    resultado_Divisão = a / b
    resultado_Divisao_inteira = a // b
    resultado_resto = a % b
    resultado_potencia = a ** b
    print("O resultado da potencia é:", resultado_potencia)
    print("O resultado da divisão por inteiro:", resultado_Divisao_inteira)
    print("O resultado do resto é:", resultado_resto)
    print("O resultado da soma é:",resultado_soma)
    print("O resultado da Subtração:", resultado_subtração)
    print("O resultado da multiplicação:",resultado_multiplicação)
    print("O resultao da divisão:", resultado_Divisão)
Número1 = int(input("Digite o primeiro Número:"))
Número2 = int(input("Digite o segundo Número:"))
calculadora(Número1, Número2)