""" Elaboração de um programa que analisa os dados dos alunos cadastrados no CIC no ano de 2019.
Esse programa tem (no mínimo) 3 inputs onde:
    - O input 1 são as Tarefas (dividida em 7 tarefas);
    - O input 2 é a quantidade de linhas que precisam ser analisadas;
    - O input 3 (em diante) são os dados a serem analisados, dividos em 6
    núimeros relacionados ao universsitário, onde:
        - Nm.1 = Ano de ingresso[0,2019];
        - Nm.2 = Dia do nascimento [1, 31];
        - Nm.3 = Mês do nascimento [1, 12];
        - Nm.4 = Ano do nascimento [0, 2019];
        - Nm.5 = Sexo [Feminino = 1, Masculino = 2];
        - Nm.6 = Situação, definido na lista:
        [2 = Cursando, 3 = Matrícula Trancada, 4 = Desvinculado do curso,
        5 = Transferido para outro curso da mesma IES, 6 = Formado, 7 = Falecido];
"""

"""Definição das Funções tarefas():
"""
#Biblioteca
import datetime
#Tarefa 1: % de universitários regulares e não regulares
def tarefa1(d6):
    if d6 == 2 or d6 == 6: #Cursando ou Formado
        return 1
    else:
        return 0

def total1_2(y, R):
    z = (R * 100)/ y #Matriculados ou formados
    a = ((y-R) * 100)/ y #Alunos em outras situações
    return z, a
#Tarefa 2: % de universitários masculinos e femininos
def tarefa2(d5):
    if d5 == 1: #Feminino
        return 0#Feminino
    else:       #Masculino
        return 1#Masculino

#Tarefa 3: Tempo médio (em anos). Considere que o ano atual seja 2019
def tarefa3(d1):
    z = 2019 - d1
    return z
    
#Tarefa 4: % dos nascimentos de de cada dia
def tarefa4(d2, d3, d4):
    x = datetime.datetime(d4, d3, d2)
    return x.strftime("%A")
#Tarefa 5: Combinação das tarefas 1 e 2
def tarefa5(d5, d6):
    if d5 == 2: #Homem
        if d6 == 2 or d6 == 6: #H_MF
            return 'H_SM'         
        else: #H_S
            return 'H_N'
    if d5 == 1: #Mulher
        if d6 == 2 or d6 == 6: #M_MF
            return 'M_SM'
        else: #M_S
            return 'M_N'
#Tarefa 6: Combinação das tarefas 1 e 3
def tarefa6(d6):
    if d6 == 2 or d6 == 6: #Cursando ou Formado
        return 'CF' #Cursando ou Formado
    else: #Demais Situações
        return 'DS' #Demais Situações
#Tarefa 7: Combinação das tarefas 2 e 4
def tarefa7(d5):
    if d5 == 1: #Feminino
        return 'F' #Cursando ou Formado
    else: #Masculino
        return 'M' #Demais Situações
# Inputs
x = int(input()) #Linha 1
y = int(input()) #Linha 2
# Variáveis
contador = 0
R = 0
Dom = 0
Seg = 0
Ter = 0
Qua = 0
Qui = 0
Sex = 0
Sab = 0
Dom1 = 0
Seg1 = 0
Ter1 = 0
Qua1 = 0
Qui1 = 0
Sex1 = 0
Sab1 = 0
H_MF = 0 #Homens Matriculados ou Formados
M_MF = 0 #Mulheres Matriculadas ou Formadas
H_S = 0 #Homens em Outras Situações
M_S = 0 #Mulheres em Outras Situações
CF = 0
DS = 0
Med_CF = 0
Med_DS = 0
H = 0
M = 0
while contador < y:
    d1, d2, d3, d4, d5, d6 = [int(z) for z in input().split()] #Linha 3 (em diante)
    if x == 1:
        R += tarefa1(d6) 
    elif x == 2:
        R += tarefa2(d5)      
    elif x == 3:
        R += tarefa3(d1)
    elif x == 4:
        dia_semana = tarefa4(d2, d3, d4)
        if dia_semana == 'Sunday':
            Dom += 1
        elif dia_semana == 'Monday':
            Seg += 1
        elif dia_semana == 'Tuesday':
            Ter += 1
        elif dia_semana == 'Wednesday':
            Qua += 1
        elif dia_semana == 'Thursday':
            Qui += 1
        elif dia_semana == 'Friday':
            Sex += 1
        else:
            Sab += 1
    elif x == 5:
        sexo_situacao = tarefa5(d5, d6)
        if sexo_situacao == 'H_SM':
            H_MF += 1
        elif sexo_situacao == 'H_N':
            H_S += 1
        elif sexo_situacao == 'M_SM':
            M_MF += 1
        if sexo_situacao == 'M_N':
            M_S += 1
    elif x == 6:
        situacao = tarefa6(d6)
        if situacao == 'CF':
            Med_CF += tarefa3(d1)
            CF += 1
        elif situacao == 'DS':
            Med_DS += tarefa3(d1)
            DS += 1
    else:
        sexo = tarefa7(d5)
        dia_semana = tarefa4(d2, d3, d4)
        if sexo == 'F':
            if dia_semana == 'Sunday':
                Dom += 1
            elif dia_semana == 'Monday':
                Seg += 1
            elif dia_semana == 'Tuesday':
                Ter += 1
            elif dia_semana == 'Wednesday':
                Qua += 1
            elif dia_semana == 'Thursday':
                Qui += 1
            elif dia_semana == 'Friday':
                Sex += 1
            else:
                Sab += 1
            M += 1
        elif sexo == 'M':
            if dia_semana == 'Sunday':
                Dom1 += 1
            elif dia_semana == 'Monday':
                Seg1 += 1
            elif dia_semana == 'Tuesday':
                Ter1 += 1
            elif dia_semana == 'Wednesday':
                Qua1 += 1
            elif dia_semana == 'Thursday':
                Qui1 += 1
            elif dia_semana == 'Friday':
                Sex1 += 1
            else:
                Sab1 += 1
            H += 1
    contador += 1

#Resposta
if x == 1 or x == 2:
    z, a = total1_2(y, R)
    if x == 1:
        print(f"matriculados ou formados:{z:5.1f}")
        print(f"alunos em outras situacoes:{a:5.1f}")
    else:
        print(f"sexo masculino:{z:5.1f}")
        print(f"sexo feminino:{a:5.1f}")
elif x == 3:
    print(f"media de anos desde ingresso:{R/y:5.1f}")
elif x == 4:
    print(f"domingo:{Dom*100/y:5.1f}")
    print(f"segunda:{Seg*100/y:5.1f}")
    print(f"terca:{Ter*100/y:5.1f}")
    print(f"quarta:{Qua*100/y:5.1f}")
    print(f"quinta:{Qui*100/y:5.1f}")
    print(f"sexta:{Sex*100/y:5.1f}")
    print(f"sabado:{Sab*100/y:5.1f}")
elif x == 5:
    print("dentre masculinos:")   
    print(f"matriculados ou formados:{(H_MF*100)/(H_MF+H_S):5.1f}")
    print(f"alunos em outras situacoes:{(H_S*100)/(H_MF+H_S):5.1f}")
    print("dentre femininos:")
    print(f"matriculados ou formados:{(M_MF*100)/(M_MF+M_S):5.1f}")
    print(f"alunos em outras situacoes:{(M_S*100)/(M_MF+M_S):5.1f}")
elif x == 6:
    print("dentre matriculados ou formados:")
    print(f"media de anos desde ingresso:{Med_CF/CF:5.1f}")
    print("dentre alunos em outras situacoes:")
    print(f"media de anos desde ingresso:{Med_DS/DS:5.1f}")
else:
    print("dentre masculinos:")
    print(f"domingo:{Dom1*100/H:5.1f}")
    print(f"segunda:{Seg1*100/H:5.1f}")
    print(f"terca:{Ter1*100/H:5.1f}")
    print(f"quarta:{Qua1*100/H:5.1f}")
    print(f"quinta:{Qui1*100/H:5.1f}")
    print(f"sexta:{Sex1*100/H:5.1f}")
    print(f"sabado:{Sab1*100/H:5.1f}")
    print("dentre femininos:")
    print(f"domingo:{Dom*100/M:5.1f}")
    print(f"segunda:{Seg*100/M:5.1f}")
    print(f"terca:{Ter*100/M:5.1f}")
    print(f"quarta:{Qua*100/M:5.1f}")
    print(f"quinta:{Qui*100/M:5.1f}")
    print(f"sexta:{Sex*100/M:5.1f}")
    print(f"sabado:{Sab*100/M:5.1f}")
