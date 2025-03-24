listaP = ['Java', 'Ruby', 'Python', 'Java', 'Python', 'Java', 'Javascript']
lista_frequencia = {}

for elemento in listaP:
    if elemento in lista_frequencia:
        lista_frequencia[elemento] += 1
    else:
        lista_frequencia[elemento] = 1
        
print(lista_frequencia)


# resolução do Samuka

# .split => irá pegar a string e irá separar em uma lista seguindo o parametro que for identificado entre os parenteses como divisor a ser considerado. No exercício usou o espaço como divisor para porder dividir os dados da string
# .keys => irá listar todas as chaves do dicionário
# .vaues => irá listar todos os valores do dicionário

def contar_frequencia(palavras):
    lista = palavras.split(' ') #vai dividir considerando o espaço como divisor entre dados
    dicionario = {}
    for palavra in lista:
        if not palavra in dicionario.keys():
            dicionario[palavra] = lista.count(palavra) # vai adicionar essa chave = com esse valor
    return dicionario

linguagens = 'Java Java Java Python Ruby Java Java Ruby Cobol Ruby Cobol Java Java C++'

print(f'Dicionario : {contar_frequencia(linguagens)}')