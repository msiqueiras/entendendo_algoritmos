#faça um algoritmo recursivo para encontrar o valor mais alto de uma lista

def max_item(lista):
    maximum = lista[0]
    if lista[1] >= maximum:
        maximum = lista[1]
    else: 
        if lista != []:
            lista.pop()
            max_item(lista)
    return maximum
            
            
l = [4, 2, 6, 3]
print('Máximo: ', max_item(l))   
