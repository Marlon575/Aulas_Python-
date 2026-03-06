Lista =[12,7,25,3,18]
maior = Lista[0] # Vou assumir que o Número da posição zero é o maior por enquanto.
for numero in Lista:
    if numero > maior:
        maior = numero
print("Maior número:",maior)