#Escreva a função soma vista anteriormente (vista em Haskell)

def soma(lista):
    s = 0
    if len(lista) == 1:
        s = lista.pop()
        return s
    else:
        s = lista.pop() + soma(lista)
        return s

l = [2, 4, 6]

soma_lista = soma(l)
print('SOMA:', soma_lista)


        