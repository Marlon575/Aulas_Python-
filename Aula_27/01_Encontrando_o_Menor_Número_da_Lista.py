Lista = [12,7,25,3,18]
menor = Lista[0]
for numero in Lista:
    if numero < menor:
        menor = numero
print("Menor número:",menor)