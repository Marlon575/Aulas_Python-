# Aula 06 - operadores avançados
# (//) Divisao inteira: Divide os numero, descarta a parte decimal e fica so com a parte inteira. Ex:7//2 = 3, numa divisao normal seria 3.5
# (%) Resto, Ex: 7 % 2 = 1( O, 1 e o resto da Divisao de 7 e 2).
# (**) Potencia, Ex: 2**3 = 8, 
valor1 = int(input("Digite o primeiro valor:"))
Valor2 = int(input("Digite o segunndo valor:"))
divisao_inteira = valor1 // Valor2
resto = valor1 % Valor2
potencia = valor1 ** Valor2
print("divisao_inteira:", divisao_inteira)
print("resto:",resto)
print("potencia:",potencia)