# Classificacao de Idade
# O programa pedi o nome e a idade(input,int),depois decide se es crianca,jovem, adulto(if,elif,else)
Nome = input("Digite seu nome:")
Idade = int(input("Digite a sua Idade"))
if Idade<15:
    print("Ola", Nome, "-Voce e crianca")
elif Idade<19:
    print("Ola", Nome ,"-Voce e Jovem")
else:
    print ("Ola", Nome ,"-voce e Adulto")