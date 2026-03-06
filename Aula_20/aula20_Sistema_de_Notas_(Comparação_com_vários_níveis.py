def verificar_nota(Nota):
    if Nota >=10:
        return "Aprovado"
    elif Nota >=7:
        return "Recuperado" # Se a primeira condição for falsa, o programa vai testar os seguintes números(7,8,9)
    else:
        return "Reprovado"
Numero = int(input("Digite a nota do aluno:"))
resultado = verificar_nota(Numero)
print("O aluno foi:",resultado)