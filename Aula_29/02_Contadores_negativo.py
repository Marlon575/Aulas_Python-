lista = []# Cria uma lista vazia
for i in range (5):# Repeter 5 vezes
    numero = int(input("Digite um número: ")) 
    lista.append(numero)# Coloca o número dentro da lista.

contador_negativo = 0 # Ceia um contador/É começa de 0

for numero in lista: # Percorre cada número da lista
    if numero < 0: # Esse número é menor que 0?/ Se for ele é negativo
        contador_negativo +=1 # Se a condição "for" verdadeira, aumenta o contador 1/

print("Quantidade de números negativos:",contador_negativo)
