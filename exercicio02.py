lista_pessoas = [('Joao', 35), ('Maria', 23), ('Carol', 18), ('Ronaldo', 22), ('Aline', 21)]

lista_ordenada = sorted(lista_pessoas, key=lambda x: x[1])

for i in lista_ordenada:
    print(i[0])