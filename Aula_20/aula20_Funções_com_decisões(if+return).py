def verificar_par(numero):
    if numero % 2 == 0: #  Decisão- Se 'numero' dividido por 2, resto(%) 0 
        return "par"
    else:
        return "ímpar"
resultado = verificar_par(4)
print(resultado)