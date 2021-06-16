""" Trabalho_ED_02
    Programador: Pedro Eduardo Cunha Ximenes
    Data: 04/05/21
    
    O objetivo deste trabalho é criar um programa
que organize a tarefa de descarga feita pelos
Wookies.
    Primeiramente é dado um valor n que representa
a quantidade de Wookies que vão realizar a tarefa.
O carregamento é representado por uma lista de
cargas C, em que uma carga é entregue por vez
seguindo uma ordem c0,c1,...,ci onde i é a
quantidade de cargas. Cada ci na lista representa
o peso da carga i, sendo c:→Z*+.
    Dispondo da entrada das cargas, o protocolo
estabelece que os Wookies devem formar uma fila e
prepararem suas pilhas para as recepções das cargas,
representados por uma fila de pilhas w, onde wi
representa a pilha do iésimo Wookiee. Salienta-se,
entretanto, que a entrega das cargas devem seguir as
seguintes regras:

        -Considerando a política do FIFO, as cargas
    sempre são entregues do primeiro Wookiee para
    o último. Caso o primeiro Wookie não possa receber
    a carga é passado para o segundo e assim se repete
    até o último Wookie.
        -Nenhum Wookie pode pegar uma segunda carga
    caso ainda tenha algum Wookiee na fila com pilha
    vazia. Em outras palavras, o Wookiee com pilha
    vazia possui prioridade.
        -Caso todos os Wookies já possuam alguma carga,
    a próxima carga será empilhada no Wookie que possui
    sua carga do topo da pilha maior ou igual que a
    carga entregue.
    
    É valido frisar que se ainda houver cargas na
lista e nenhum Wookie for capaz de pegá-las essas
devem ser postas em uma lista s de sobras, seguindo
a mesma ordem de chegada da lista c.
    Ao término, os Wookies devem se apresentar em
uma fila ordenada decrescente pelo peso que cada
Wookiee carrega. O peso é a soma de todas as
cargas que estão na pilha do Wookiee. Além disso,
deve ser fornecida uma lista com as cargas que
sobraram após a finalização da primeira etapa.
"""
def adiciona_carga(lista_c, lista_w, lista_s):
    for wookie in lista_w:
        if lista_c != []:
            wookie.append(lista_c.pop(0))
    
        else:
            return lista_w, lista_s
    
    for carga in lista_c:
        c = True
        for wookie in lista_w:
            if carga <= wookie[len(wookie) - 1]:
                wookie.append(carga)
                c = False
                break
        
        if c:
            lista_s.append(carga)
    
    return lista_w, lista_s


def soma(a):
    
    return sum(a)


quant_wookies = int(input())
soubra = input()
lista_cargas = ([int(x) for x in soubra.split()])
lista_wookies = list()
lista_sobras = list()
if quant_wookies == 0:
    print('Os Wookies foram para o lado sombrio da força!')
    print(soubra)

else:
    for x in range(quant_wookies):
        lista_wookies.append([])

    wookies, sobras = adiciona_carga(lista_cargas, lista_wookies, lista_sobras)
    wookies.sort(reverse = True, key = soma)
    for w in wookies:
        print(w, end = ' ')
        
    print('')

    if sobras == []:
        print('A força está com os Wookies!')
        
    else:
        for s in sobras:
            print(s, end = ' ')
            
        print('')
