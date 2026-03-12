lista = [] # Creia uma lista vazia.
for i in range(5): # O programa vai repetir 5 vezes os proximos comandos dentro dele.
    numero =int(input("Digite os números:"))
    lista.append(numero) # Entrudos os números entroduzidos na varialvel numero, a listas.
maior = lista[0] # Define o primeiro número da lista como maior,nu momento.
posicao = 0 # Guarda a posição inicial do maior número.
for i in range(len(lista)): #Percorre todas as posições da lista.
    if lista[i] > maior: #verifica se o número da posição i é maior/ lista[i] são as posições da lista.
        maior = lista[i] # Guarda o novo maior e passa a ser o número encontrado.
        posicao = i # Guarda a posição do novo maior número
print("Maior número é :", maior)
print("Posoção do maior:", posicao)


