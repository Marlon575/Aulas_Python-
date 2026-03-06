Número_final = int(input("Digite o número:"))
soma = 0  # Criamos uma caixa chamada soma, essa caixa começa do 0, e vai guardar o total.
for numero in range (1, Número_final + 1):
    soma = soma + numero # EX: Digitando 5 (1,3,3,4,5)-
#Ele vai pegar esses numeros e somar um pelo outro e guarda o valor na caixa soma que ccomeca em zero 0
# 1+2+3+4+5=15
print ("A soma total é:",soma)