#escreva um algoritmo recursivo que conte a quantidade de elementos de uma lista

def qnt_elementos(lista):
    qnt = 0
    if lista == []:
        return 0
    qnt = 1 + qnt_elementos(lista[1:])
    return qnt
    
l = [3, 4, 5, 6, 7]
print("Quantidade de elementos: ", qnt_elementos(l))