"""Dada uma imagem conte quantos pixels tem valor maior do que metade do valor máximo que um pixel pode assumir na imagem.

Essa operação é muito simples e bastante útil. Por exemplo, dada uma imagem contendo apenas um número escrito à mão, tal
como nas caixinhas do campo de código postal em envelopes do correio, é possível distinguir o número 1 do número 8 usando
essa simples contagem.

Nesta questão, a imagem é fornecida no formato NetPBM ASCII, ou seja, um arquivo PNM do tipo P1, P2 ou P3. Trata-se de um
formato que permite que imagens sejam editadas em qualquer editor de texto, pois além da imagem não ser comprimida, os
dados são salvos em formato de texto e com uma estrutura muito simples. Além disso, o formato é altamente disseminado,
qualquer visualizador de imagens padrão no Linux é capaz de exibi-las.

A documentação completa desse formato encontra-se em seu site oficial.

Essencialmente, o arquivo possui um cabeçalho contendo 3 ou 4 itens (dependendo do tipo de imagem), o qual é seguido por
uma sequência de números que indica o valor de cada pixel. A seguir, fornecemos mais detalhes."""
#Bibliotecas
import os

#Fuções
def qual_tipo():
    tipo = lista_foto[0].split()
    return tipo[0]
    
def numeros_maiores():
    soma = 0
    for x in lista_foto:
            a = x.split()
            for y in range(len(a)):
                lista_valores.append(a[y])
    max_val = int(lista_valores[3])
    if tipo == 'P1':       
        for x in lista_valores[3:]:
            for y in range(len(x)):
                if x[y] != ' ':
                    valor_num.append((int(x[y])))
        soma = sum(valor_num)
    elif tipo == 'P2' or tipo == 'P3':
        for x in lista_valores[4:]:
            for y in x.split():
                if tipo == 'P2':
                    if int(y) > max_val/2:
                        soma +=1
                elif tipo == 'P3':
                    if y.isnumeric() == True:
                        lista_valores_P3.append(int(y))
        if tipo == 'P3':
            cont1 = 0
            while cont1 < len(lista_valores_P3):
                som = 0
                cont = 0
                while cont < 3:
                    som += lista_valores_P3[cont + cont1]
                    cont += 1
                if som/3 > max_val/2:
                    soma += 1
                cont1 += 3              
    print(soma)

#Iteráveis
lista_foto = [] #Lista inicial para armazenar os dados (Não deve ser usada para os calculos de numeros maiores que o max_val
lista_valores = []
lista_valores_P3 = []
valor_num = [] #Valores dos bits no P1

#Início do Programa
foto = input()
if os.path.isfile(foto):
    with open(foto, 'r') as arquivo:
        arquivo_foto = list(arquivo)
        for lista in arquivo_foto:
            if lista[0] != '#':
                lista_foto.append(lista.rstrip())
        
        tipo = qual_tipo()
        numeros_maiores()