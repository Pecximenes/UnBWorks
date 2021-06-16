'''Funções'''
def criacao_de_lista(lista_geral, N):
    cont = 0
    while cont < N:
        lista_individual = input().split()
        lista_geral.append(lista_individual)
        cont += 1
        
    return lista_geral


def criacao_de_resultados(resultados, n_train):
    cont = 0
    lista_resultados = []
    while cont < n_train:
        lista_resultados.append(input())
        cont += 1
        
    return lista_resultados


def modificador__de_lista(lista_geral):
    grupo_de_listas = [['b', 'c', 'x', 'f', 'k', 's'],
                       ['f', 'g', 'y', 's'],
                       ['n', 'b', 'c', 'g', 'r', 'p', 'u', 'e', 'w', 'y'],
                       ['t', 'f'],
                       ['a', 'l', 'c', 'y', 'f', 'm', 'n', 'p', 's'],
                       ['a', 'd', 'f', 'n'],
                       ['c', 'w', 'd'],
                       ['b', 'n'],
                       ['k', 'n', 'b', 'h', 'g', 'r', 'o', 'p', 'u', 'e', 'w', 'y'],
                       ['e', 't'],
                       ['b', 'c', 'u', 'e', 'z', 'r', '?'],
                       ['f', 'y', 'k', 's'],
                       ['f', 'y', 'k', 's'],
                       ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'],
                       ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'],
                       ['p', 'u'],
                       ['n', 'o', 'w', 'y'],
                       ['n', 'o', 't'],
                       ['c', 'e', 'f', 'l', 'n', 'p', 's', 'z'],
                       ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y'],
                       ['a', 'c', 'n', 's', 'v', 'y'],
                       ['g', 'l', 'm', 'p', 'u', 'w', 'd']]
    for lista in lista_geral:
        cont1 = 0
        while cont1 < 22:
            lista[cont1] = grupo_de_listas[cont1].index(lista[cont1])
            cont1 += 1
            
    return lista_geral


def calcula_media(lista_geral_com_numeros, N): #Função que calcula a média
    cont1, lista_de_medias = 0, []
    while cont1 < 22:
        soma, cont = 0, 0
        while cont < N:
            soma += lista_geral_com_numeros[cont][cont1]
            cont += 1
            
        med = soma/N
        lista_de_medias.append(med)
        cont1 +=1
        
    return lista_de_medias


def calcula_desvio_padrao(lista_geral_com_numeros, lista_de_medias, N): 
    cont1, lista_de_desvio = 0, []
    while cont1 < 22:
        soma, cont = 0, 0
        while cont < N:
            soma += (lista_geral_com_numeros[cont][cont1] - lista_de_medias[cont1])**2
            cont += 1
            
        desv = (soma/N)**(1/2)
        lista_de_desvio.append(desv)
        cont1 +=1
        
    return lista_de_desvio
    
    
def igualar_atributo(lista_geral_com_numeros, lista_de_medias, lista_de_desvio):
    for lista in lista_geral_com_numeros:
        cont = 0
        while cont < 22:
            lista[cont] = (lista[cont] - lista_de_medias[cont])
            if lista_de_desvio[cont] == 0.0:
                lista[cont] = 0.0
                
            else:
                lista[cont] = lista[cont]/lista_de_desvio[cont]
                
            cont += 1
            
    return lista_geral_com_numeros


def calcula_distancia_euclidiana(lista_geral_igualado_test, lista_geral_igualado_train, n_train, n_test): #Função que calcula o desvio padrão
    distancia_euclidiana = []
    for lista in lista_geral_igualado_test:
        lista_de_distancia = []
        cont1, dist = 0, 0
        while cont1 < n_train:
            soma, cont = 0, 0
            while cont < 22:
                soma += (lista[cont] - lista_geral_igualado_train[cont1][cont])**2
                cont += 1
                
            dist = soma**(1/2)
            lista_de_distancia.append(dist)
            cont1 +=1
            
        distancia_euclidiana.append(lista_de_distancia)
        
    return distancia_euclidiana


def achar_valor (resultados, lista_de_distancia, k):   
    lista_sorteada, lista_sorteada1 = [], []
    for lista1 in lista_de_distancia:
        lista_sorteada.append(list(map(float, lista1)))
        
    for lista in lista_sorteada:
        lista.sort()
        lista_sorteada1.append(lista[:k])
        
    cont1 = 0
    for lista in lista_sorteada1:
        cont, lista_de_resultados = 0, []
        while cont < k:
            num = lista_de_distancia[cont1].index(lista[cont])
            lista_de_resultados.append(resultados[num])
            cont += 1
        
        p = lista_de_resultados.count('p')
        e = lista_de_resultados.count('e')
        if p > e:
            print('p')
            
        else:
            print('e')
            
        cont1 += 1
        
    return lista_sorteada1


'''Início do Programa'''
#Tarefa 1
k = int(input())

#Tarefa 2 e 3
n_train, n_test = [int(z) for z in input().split()]

#Tarefa 4
lista_geral = []
criacao_de_lista(lista_geral, n_train)

#Tarefa 5
lista_geral_com_numeros = modificador__de_lista(lista_geral)

#Tarefa 6
lista_de_medias = calcula_media(lista_geral_com_numeros, n_train)
lista_de_desvio = calcula_desvio_padrao(lista_geral_com_numeros,
                                        lista_de_medias, n_train)

#Tarefa 7
lista_geral_igualado_train = igualar_atributo(lista_geral_com_numeros,
                                              lista_de_medias, lista_de_desvio)

#Tarefa 8
resultados = []
resultados = criacao_de_lista(resultados, n_train)

#Tarefa 9
lista_geral_teste = []
criacao_de_lista(lista_geral_teste, n_test)

#Tarefa 10
lista_geral_com_numeros_teste = modificador__de_lista(lista_geral_teste)
lista_geral_igualado_test = igualar_atributo(lista_geral_com_numeros_teste,
                                             lista_de_medias, lista_de_desvio)

#Tarefa 11
lista_de_distancia = calcula_distancia_euclidiana(lista_geral_igualado_test,
                                                  lista_geral_igualado_train,
                                                  n_train, n_test)
lista_sorteada = achar_valor(resultados, lista_de_distancia, k)
