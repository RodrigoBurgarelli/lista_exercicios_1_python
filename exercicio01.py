numeros = [1, 2, 5, 6, 4, 8, 9]

def somar_numeros(numeros):
      
    soma = 0
    
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    return soma
        
resultado = somar_numeros(numeros)

print("A soma dos pares é: ", resultado)