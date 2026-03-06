# Regra mais importante:
# Nunca escreva um código primeiro.
# Primeiro pense,depois programa.

#EX:
# Um programa deve dizer se a pessoa pode votar.

# Pensamento passo a passo:
# 1. Pergunta a Idade
# 2. Guarda a Idade
# 3. Verifica e decide se pode votar, se idade >=18
Idade =int(input("Digita a sua idade:"))
if Idade>=18:
    print("Voce pode votar")
else:
    print("Voce não pode votar")

# Truque de programador
# antes de programar, responde sempre:
# O que entra? (input)
# O que o Programa decide?
# O que sai? (pouput)

Idade = int(input("Digite a sua idade:"))
if Idade>=20:
    print("Voce pode dirigir")
else:
    print("Voce não pode dirigir")