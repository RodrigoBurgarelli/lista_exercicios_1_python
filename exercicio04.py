frase = 'essa lista de exercícios está deixando muitas pessoas de cabelo em pé ou até mesmo sem cabelo'

frase_separada = frase.split()

contagem = {}

for elemento in frase_separada:
    if elemento in contagem:
        contagem [elemento] += 1
    else:
        contagem [elemento] = 1


print(contagem)
