# O programa pede a Idade da Pessoa, e decide se e crianca,jovem,adulto(if,elif,else).E mostra o resoltado no ecra(print)
Idade = int(input("Digite sua idade:")) 
if Idade < 13:
    print("Voce é criança")
elif Idade <18:
    print(" Voce é jovem")
else:
    print("Voce é adulto")