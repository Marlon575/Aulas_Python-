def verificador_maior(n):
    if n >10:
        return "Maior que 10"
    elif n <10:
        return "Menor que 10"
    else:
        return "O número 10"
numero =int(input("Digite um número:"))
resultado = verificador_maior(numero)
print("O número insirido é :", resultado)