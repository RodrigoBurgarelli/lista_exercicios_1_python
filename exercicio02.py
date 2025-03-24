lista_pessoas = [('Joao', 35), ('Maria', 23), ('Carol', 18), ('Ronaldo', 22), ('Aline', 21)]

list_ordenada = sorted(lista_pessoas, key=lambda x: x[1])

for i in list_ordenada:
    print(i[0])
    
    

# resolução apresentada pelo Samuka

#sorted() => cria uma cópia
#sort() => modifica a lista original
#lambda => a lambda tem o mesmo conceito da função anonima de javascript () = {}
# lambda é seguido da chave de ordenação: chave de ordenação [posição a ser considerada para ordenação] => key=lambda x: x[1]
# Lambda => se quiser ordem descrescente é só colocar no final reverse=true


def ordenar_tuplas(lista_tuplas):
    lista_ordenada = sorted(lista_tuplas, key= lambda tupla: tupla[1])
    return lista_ordenada

lista_de_tuplas = [('Samuel', 23),('Karynne', 20),('Carol', 21),('Edu', 15)]

print(f'A lista de tuplas ordenada por idade: {ordenar_tuplas(lista_de_tuplas)}')