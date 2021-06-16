""" Trabalho_ED_01
    Programador: Pedro Eduardo Cunha Ximenes
    Data: 29/03/21
    
    O objetivo principal deste trabalho é resolver
um problema específico de um personagem imaginário,
onde esse está dividido em 2 etapas:
    Etapa 1 - Decodificação da lista de missões
    Etapa 2 - Selecionar Subconjunto de missões

    A realização desta tarefa compreende os
conteúdos: Análise de Algoritmos; Estrutura de
Dados Básica; Recursão. Para facilitar, na correção
já está implementado a classe Deque:"""

from deque import Deque
# Obs- Não é necessário acrescentar esta biblioteca na correção
   
""" O objetivo deste programa é decodificar as
missões criptografadas fornecida pelo corretor
através da cifra de Cézar (o corretor também dará
a chave para a decodificação). A outra parte do
objetivo é calcular qual é o conjunto de missões
mais lucrativos em um dado intervalo de tempo para
realizalas."""

'''Primeira Tarefa'''
# Função com o objetivo de adicionar o alfabeto ao deque.
def adicionar_alfabeto(deque, alfabeto):
    for letra in alfabeto:
        deque.add_front(letra)
    
    return None



# Função que decifra o texto cifrado.
def decifrar(d, texto_cifrado, chave):
    alfabeto = d.__str__()
    
    for movimento in range(chave):
        letra = d.remove_front()
        d.add_rear(letra)
    
    alfabeto_cifrado = d.__str__()
    texto_descifrado = str()
       
    for letra in texto_cifrado:
        local = alfabeto.find(letra)
        letra_descifrada = alfabeto_cifrado[local]
        texto_descifrado = texto_descifrado + letra_descifrada
        
    while d.__str__()[0] != texto_descifrado[len(texto_descifrado) - 1]:
        letra = d.remove_front()
        d.add_rear(letra)
        
    return texto_descifrado
        


'''Segunda Tarefa'''
# Função que organiza a ordem das informações
def organizar_ordem(ordem):
    '''0 = Nome da Missão
       1 = Duração
       2 = Valor
       3 = Nível de Dificuldade'''   
    if ordem == 0: # (0, 1, 2, 3)
        ordem_saida = ['Nome', 'Duração', 'Valor', 'Dificuldade']
    
    elif ordem == 1: # (1, 0, 2, 3)
        ordem_saida = ['Duração', 'Nome', 'Valor', 'Dificuldade']
    
    elif ordem == 2: # (2, 0, 1, 3)
        ordem_saida = ['Valor', 'Nome', 'Duração', 'Dificuldade']
    
    elif ordem == 3: # (3, 0, 1, 2)
        ordem_saida = ['Dificuldade', 'Nome', 'Duração', 'Valor']

    return ordem_saida


#
def transforma_lista(missao, conj_missao):
    lista_missao = missao.split(',')
    ordem_entrada = ['Nome', 'Duração', 'Valor', 'Dificuldade'] # (0, 1, 2, 3)
    dicio = dict()
    
    for num in range(4):
        if ordem_entrada[num] == 'Duração' or ordem_entrada[num] == 'Valor':
            dicio.update({ordem_entrada[num]: int(lista_missao[num])})
            
        else:
            dicio.update({ordem_entrada[num]: lista_missao[num]})
            
    return dicio



# Função
def calculo_melhor_valor(conj_missao, tempo_total, matriz, quant_missao):
    '''Matriz melhor é formado por:
        Colunas (Tempo) = len(matriz[0])
        Linhas (Quantidade de missões) = len(matriz)'''
    '''for zero in range(num_de_missoes + 1):
        matriz_melhor_valor[zero].append(0)
    
    for zero in range(quant_hrs_disp):
        matriz_melhor_valor[0].append(0)'''
    
    for linha in range(1, quant_missao + 1):
        for coluna in range(1, tempo_total + 1):
            if conj_missao[linha - 1]['Duração'] > coluna:
                matriz[linha].append(matriz[linha - 1][coluna])
            
            else:
                usa = conj_missao[linha - 1]['Valor'] + matriz[linha - 1][coluna - conj_missao[linha - 1]['Duração']]
                nao_usa = matriz[linha - 1][coluna]                  
                
                if usa > nao_usa:
                        matriz[linha].append(usa)
                
                else:
                    matriz[linha].append(nao_usa)
    
    missoes_usadas = []
    tempo = tempo_total
    missao = quant_missao
    while missao >= 1:
        if matriz[missao][tempo] == matriz[missao - 1][tempo - conj_missao[missao - 1]['Duração']] + conj_missao[missao - 1]['Valor']:
            missoes_usadas.append(missao)
            tempo = tempo - conj_missao[missao - 1]['Duração']
        missao = missao - 1
    
    return matriz, missoes_usadas



#
def maior_menor_igual(nome1, nome2, d):
    '''Índice:
        Iguais = 1
        Nome1 vem antes = 1
        Nome2 vem antes = 2'''
    alfabeto = str(d)
    if nome1 == nome2:
        return 1
    
    if len(nome1) > len(nome2):
        maior = nome1
    
    else:
        maior = nome2
    
    for i in range (len(maior)):
        letra_nome1 = nome1[i] #Abacaxi
        letra_nome2 = nome2[i] #Pessego
        if alfabeto.find(letra_nome1) < alfabeto.find(letra_nome2) or i == len(nome1) - 1:
            return 1
        
        elif alfabeto.find(letra_nome1) > alfabeto.find(letra_nome2) or i == len(nome2) - 1:
            return 2



# Função que organiza a saída do programa
def organizador_de_lista(ordem_alfabetica, nome1, d, dicionario, ordem):
    tamanho = len(ordem_alfabetica)
    primeiro = ordem[0]
    if ordem_alfabetica == [] or (maior_menor_igual(nome1, str(ordem_alfabetica[tamanho // 2][primeiro]), d) == 2 and tamanho == 1):
        ordem_alfabetica.append(dicionario)
    
    elif maior_menor_igual(nome1, str(ordem_alfabetica[0][primeiro]), d) == 1:
        ordem_alfabetica.insert(0, dicionario)
    
    elif maior_menor_igual(nome1, str(ordem_alfabetica[tamanho// 2][primeiro]), d) == 1:
        valor = organizador_de_lista(ordem_alfabetica[:tamanho // 2], nome1, d, dicionario, ordem)
        valor.extend(ordem_alfabetica[tamanho // 2:])
        ordem_alfabetica = valor
        
    elif maior_menor_igual(nome1, str(ordem_alfabetica[tamanho// 2][primeiro]), d) == 2:
        valor = organizador_de_lista(ordem_alfabetica[tamanho // 2:], nome1, d, dicionario, ordem)
        ordem_alfabetica = ordem_alfabetica[:tamanho // 2]
        ordem_alfabetica.extend(valor)
            
    else:
        ordem_alfabetica.insert((tamanho // 2) + 1, dicionario)
        
    return ordem_alfabetica



#
def organizador_de_lista1(primeiro, ordem, d):
    tamanho = len(primeiro)
    for j in range(tamanho + 10):
        for i in range(tamanho):
            if len(primeiro) == i + 1:
                break
            if primeiro[i][ordem[0]] == primeiro[i + 1][ordem[0]]:
                nome1 = primeiro[i][ordem[1]]
                nome2 = primeiro[i + 1][ordem[1]]
                num = maior_menor_igual(nome1, nome2, d)
                if num == 2:
                    dic = primeiro[i + 1]
                    primeiro.remove(dic)
                    primeiro.insert(i, dic)
    
    return primeiro



# Função principal onde se recebe as informações para calcular as outras funções
def selecionar_subconjunto_missoes():
    quant_hrs_disp = int(input())
    mostra_missao = int(input())
    
    if mostra_missao == 0:
        mostra_missao = False
        
    elif mostra_missao == 1:
        mostra_missao = True

    '''Ordem das informações sendo:
        0 = Nome da Missão
        1 = Duração
        2 = Valor
        3 = Nível de Dificuldade'''
    ordem = int(input()) # Ordem das informações      
    alfabeto = input()
    chave = int(input())
    num_de_missoes = int(input())
    d = Deque()
    matriz_melhor_valor = [[]]
    conjunto_missao = list()
    
    adicionar_alfabeto(d, alfabeto)
    ordem = organizar_ordem(ordem)
    
    for vez in range(num_de_missoes):
        matriz_melhor_valor.append([]) # Linhas(Missões)
        texto_cifrado = input().lstrip('[').rstrip(']')
        missao = (decifrar(d, texto_cifrado, chave))
        conjunto_missao.append(transforma_lista(missao, conjunto_missao))
        
    if quant_hrs_disp == 0:
        tempo_restante = 0
        valor = 0
            
    else:
        for zero in range(num_de_missoes + 1):
            matriz_melhor_valor[zero].append(0)
        
        for zero in range(quant_hrs_disp):
            matriz_melhor_valor[0].append(0)
            
        matriz_melhor_valor, missoes_usadas = calculo_melhor_valor(conjunto_missao, quant_hrs_disp, matriz_melhor_valor, num_de_missoes)    
        valor = matriz_melhor_valor[num_de_missoes][quant_hrs_disp]
        lista_missoes_escolhidas = list()
        
        for missao in missoes_usadas:
            lista_missoes_escolhidas.append(conjunto_missao[missao - 1])
        
        if mostra_missao:
            lista_ordem_alfabetica_primeiro = list()
            for dicionario in lista_missoes_escolhidas:
                nome1 = str(dicionario[ordem[0]])
                lista_ordem_alfabetica_primeiro = organizador_de_lista(lista_ordem_alfabetica_primeiro, nome1, alfabeto, dicionario, ordem)
            
            if ordem[0] == 'Nome':                
                lista_final = lista_ordem_alfabetica_primeiro
            
            else:
                lista_final = organizador_de_lista1(lista_ordem_alfabetica_primeiro, ordem, alfabeto)
            
            for dic in lista_final:
                print(f'{dic["Nome"]}, {dic["Duração"]}, {dic["Valor"]}, {dic["Dificuldade"]}')
        
        else:
            lista_final = lista_missoes_escolhidas
        
        duracao = 0
        for dic in lista_final:
            duracao += dic['Duração']
    
        tempo_restante = quant_hrs_disp - duracao
    print(f'Tempo restante: {tempo_restante}')
    print(f'Valor: {valor}')
    
    return None



selecionar_subconjunto_missoes()