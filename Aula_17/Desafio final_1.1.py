def calculadora ():
    Numero1 = float(input("Digite o primeiro número:"))
    Numero2 = float(input("Digite o segundo número:"))
    resultado_soma = Numero1 + Numero2
    resultado_subtração = Numero1 - Numero2
    resultado_multiplicação = Numero1 * Numero2
    resultado_divisão = Numero1 / Numero2
    resultado_divisão_inteira = Numero1 // Numero2
    resultado_resto_da_divisão = Numero1 % Numero2
    resultado_potencia = Numero1 ** Numero2
    print("O resultado da potencia:", resultado_potencia)
    print("O resultado do resto da divisão:",resultado_resto_da_divisão)
    print("O resultado da divisão por inteira:",resultado_divisão_inteira)
    print("O resultado da soma:",resultado_soma)
    print("O resultado da subtração:",resultado_subtração)
    print("O resultado da multiplicação:",resultado_multiplicação)
    print("O resultado da divisão:", resultado_divisão)
calculadora()