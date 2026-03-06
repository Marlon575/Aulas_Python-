# O um contador é uma variálvel que começa em 0 e aumenta toda vez que algo acontece.
contador = 0 # Cria uma variável chamada "contador"./Ele começa com valor 0, por ainda não contamos nada.
for i in range (5): # Repite o bloco abaixo 5 vezes/range(5)gera:0,1,2,3,4.
    contador += 1 # Pegue o valor atual de "contador" e  some  com 1
print(contador)