lista = ['Java', 'Ruby', 'Python', 'Java', 'Python', 'Java', 'Javascript']
lista_frequencia = {}

for elemento in lista:
    if elemento in lista_frequencia:
        lista_frequencia[elemento] += 1
    else:
        lista_frequencia[elemento] = 1
        
print(lista_frequencia)