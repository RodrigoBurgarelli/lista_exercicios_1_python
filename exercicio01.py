numeros = [1,4,6,10,13,8,2,9,10,2,5]

def somar_numeros(numeros):
      
    soma = 0
    
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    return soma
        
resultado_soma = somar_numeros(numeros)

print("A soma dos pares é: ", resultado_soma)



# forma apresentada pelo Samuka

def somar_pares(Lista_de_numeros):
    resultado = 0
    for numero in Lista_de_numeros:
        if numero % 2 == 0:
            resultado += numero
    return resultado

lista = [1,4,6,10,13,8,2,9,10,2,5]

print(f'O resultado da soma dos elementos pares é: {somar_pares(lista)}')