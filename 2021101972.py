import random
from os import system, name 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2021101972" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "JOAO VITOR DE OLIVEIRA ROSARIO" 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

def jogadaComputador(L1,Simbolo):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador
    
    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia
    O jogo e definido nos 4 primeiro turno, caso o computador seja o primeiro 
    a jogar ele fara aleatoriamente 2 jogadas pragramas,caso ele nao seja o primeiro
    as jogadas serao de formas defensivas, reagindo a jogadas do usuario
    """
    p1 = L1[1]
    p2 = L1[2]
    p3 = L1[3]
    p4 = L1[4]
    p5 = L1[5]
    p6 = L1[6]
    p7 = L1[7]
    p8 = L1[8]
    p9 = L1[9]
    Turno = turno(L1[1:],n = 0,b = 0)
    if Simbolo == "X":
        inimigo = "O"
    else:
        inimigo = "X"
    if Turno == 1:
        ax = random.choice([1, 3, 7,9])
        az = 5
        Local = random.choice([ax,az])
    if Turno == 2:
        if p5 == " ":
            Local = 5
        else:
            Local = random.choice([1,3,7,9])
    if Turno == 3:
        if p5 == " ":
            Local = 5
        else:
            if p2 == inimigo or p4 == inimigo or p8 == inimigo or p6 == inimigo:
                Local = random.choice([1, 3, 7,9])
            else:
                if p3 == inimigo:
                    Local = 7
                if p1 == inimigo:
                    Local = 9
                if p7 == inimigo:
                    Local = 3
                if p9 == inimigo:
                    Local = 1
                if p5 == inimigo:
                    if p1 == Simbolo:
                        Local = 9
                    if p3 == Simbolo:
                        Local = 7
                    if p7 == Simbolo:
                        Local = 3
                    if p9 == Simbolo:
                        Local = 1
    if Turno == 4:
        a = VaiganharVaiperde(L1,Simbolo)
        b = VaiganharVaiperde(L1,inimigo)
        if a != None  or b != None :
            if a != None:
                Local = a
            else:
                if b !=None:
                    Local = b
        else:
            Local =  "ab"
            if p1 == p9 and p1 == inimigo:
                Local = random.choice([2,4,8,6])
            if p3 == p7 and p3 == inimigo:
                Local = random.choice([2,4,8,6])
            if p9 == p4 and p9 == inimigo:
                Local = random.choice([1])
            if p9 == p2 and p9 == inimigo:
                Local = random.choice([1])
            if p7 == p2 and p7 == inimigo:
                Local = random.choice([3])
            if p7 == p6 and p7 == inimigo:
                Local = random.choice([3])
            if p1 == p8 and p1 == inimigo:
                Local = random.choice([9])
            if p1 == p6 and p1 == inimigo:
                Local = random.choice([9])
            if p3 == p4 and p3 == inimigo:
                Local = random.choice([7])
            if p3 == p8 and p3 == inimigo:
                Local = random.choice([7])     
            if p4 == p8 and p4 == inimigo:
                Local = random.choice([7,9,1])
            if p8 == p6 and p8 == inimigo:
                Local = random.choice([7,9,3])
            if p6 == p2 and p6 == inimigo:
                Local = random.choice([3,1,9])
            if p2 == p4 and p2 == inimigo:
                Local = random.choice([1,7,3])
            if p7 == p5 and p5 == inimigo:
                Local = random.choice([1,9])
            if p9 == p5 and p5 == inimigo:
                Local = random.choice([7,3])
            if p3 == p5 and p5 == inimigo:
                Local = random.choice([1,9])
            if p1 == p5 and p5 == inimigo:
                Local = random.choice([7,3])
            if Local == "ab":
                Local == random.choice([1,2,3,4,5,6,7,8,9])
    if Turno == 5:
        a = VaiganharVaiperde(L1,Simbolo)
        b = VaiganharVaiperde(L1,inimigo)
        if a != None  or b != None :
            if a != None:
                Local = a
            else:
                if b !=None:
                    Local = b
        else:
            Local = random.choice([1,2,3,4,5,6,7,8,9])
    if Turno == 6:
        a = VaiganharVaiperde(L1,Simbolo)
        b = VaiganharVaiperde(L1,inimigo)
        if a != None  or b != None :
            if a != None:
                Local = a
            else:
                if b !=None:
                    Local = b
        else:
            Local = random.choice([1,2,3,4,5,6,7,8,9])
    if Turno == 7:
        a = VaiganharVaiperde(L1,Simbolo)
        b = VaiganharVaiperde(L1,inimigo)
        if a != None  or b != None :
            if a != None:
                Local = a
            else:
                if b !=None:
                    Local = b
        else:
            Local = random.choice([1,2,3,4,5,6,7,8,9])
    if Turno == 8:
        a = VaiganharVaiperde(L1,Simbolo)
        b = VaiganharVaiperde(L1,inimigo)
        if a != None  or b != None :
            if a != None:
                Local = a
            else:
                if b !=None:
                    Local = b
        else:
            Local = random.choice([1,2,3,4,5,6,7,8,9])
    if Turno == 9:
        a = VaiganharVaiperde(L1,Simbolo)
        b = VaiganharVaiperde(L1,inimigo)
        if a != None  or b != None :
            if a != None:
                Local = a
            else:
                if b !=None:
                    Local = b
        else:
            Local = random.choice([1,2,3,4,5,6,7,8,9])

    if Local == 1 or Local == 2 or Local == 3:
        if L1[Local] == " ":
            return Local
        else:
            return jogadaComputador(L1,Simbolo)
    if Local == 4 or Local == 5 or Local == 6:
        if L1[Local] == " ":
            return Local
        else:
            return jogadaComputador(L1,Simbolo)
    if Local == 7 or Local == 8 or Local == 9:
        if L1[Local] == " ":
            return Local
        else:
            return jogadaComputador(L1,Simbolo)

def turno(L,n = 0,b = 0):
    """
    Funçao responsavel por verificar quantas jogadas foram feitas

    Paramentros 
    L = lista
    n = posiçao na lista
    b = numero de espaços vazios

    return Turno
    """

    if n == 9:
        Turno = 10 - b
        return Turno
    else:
        if L[n]== " ":
            return turno(L,n+1,b+1)
        else:
            return turno(L,n+1,b)
        


def VaiganharVaiperde(L1,simbolo):
    """
    Funçao que recebe o tabuleiro, e o simbolo(X/O) e verifica 
    dependendo do referencial , se ha possibilidade de ganhar ou perder

    parametros
    L1 = Lista contendo os valores do tabuleiro
    simbolo = Letra do jogador

    """
    #Perder na horizontal
    if L1[1] == L1[2] or L1[2] == L1[3] or L1[1] == L1[3]:
        if L1[1] == L1[2] and L1[1] == simbolo and L1[3] == " ":
            return 3
        if L1[2] == L1[3] and L1[2] == simbolo and L1[1] == " ":
            return 1
        if L1[1] == L1[3] and L1[1] == simbolo and L1[2] == " ":
            return 2
    if L1[4] == L1[5] or L1[5] == L1[6] or L1[4] == L1[6]:
        if L1[4] == L1[5] and L1[4] == simbolo and L1[6] == " ":
            return 6
        if L1[5] == L1[6] and L1[5] == simbolo and L1[4] == " ":
            return 4
        if L1[4] == L1[6] and L1[4] == simbolo and L1[5] == " ":
            return 5
    if L1[7] == L1[8] or L1[8] == L1[9] or L1[7] == L1[9]:
        if L1[7] == L1[8] and L1[7] == simbolo and L1[9] == " ":
            return 9
        if L1[8] == L1[9] and L1[8] == simbolo and L1[7] == " ":
            return 7
        if L1[7] == L1[9] and L1[7] == simbolo and L1[8] == " ":
            return 8
    #Perde na Vertical
    if L1[1] == L1[4] or L1[4] == L1[7] or L1[1] == L1[7]:
        if L1[1] == L1[4] and L1[1] == simbolo and L1[7] == " ":
            return 7
        if L1[4] == L1[7] and L1[4] == simbolo and L1[1] == " ":
            return 1
        if L1[1] == L1[7] and L1[1] == simbolo and L1[4] == " ":
            return 4
    if L1[2] == L1[5] or L1[5] == L1[8] or L1[2] == L1[8]:
        if L1[2] == L1[5] and L1[2] == simbolo and L1[8] == " ":
            return 8
        if L1[5] == L1[8] and L1[5] == simbolo and L1[2] == " ":
            return 2
        if L1[2] == L1[8] and L1[2] == simbolo and L1[5] == " ":
            return 5
    if L1[3] == L1[6] or L1[6] == L1[9] or L1[3] == L1[9]:
        if L1[3] == L1[6] and L1[3] == simbolo and L1[9] == " ":
            return 9
        if L1[6] == L1[9] and L1[6] == simbolo and L1[3] == " ":
            return 3
        if L1[3] == L1[9] and L1[3] == simbolo and L1[6] == " ":
            return 6
    #Perde na diagonal
    if L1[1] == L1[5] or L1[5] == L1[9] or L1[1] == L1[9]:
        if L1[1] == L1[5] and L1[1] == simbolo and L1[9] == " ":
            return 9
        if L1[5] == L1[9] and L1[5] == simbolo and L1[1] == " ":
            return 1
        if L1[1] == L1[9] and L1[1] == simbolo and L1[5] == " ":
            return 5
    if L1[3] == L1[5] or L1[5] == L1[7] or L1[3] == L1[7]:
        if L1[3] == L1[5] and L1[3] == simbolo and L1[7] == " ":
            return 7
        if L1[5] == L1[7] and L1[5] == simbolo and L1[3] == " ":
            return 3
        if L1[3] == L1[7] and L1[3] == simbolo and L1[5] == " ":
            return 5
def Letra():
    """
    Funçao que retorna  a letra (X/O) que o jogador escolher

    """
    Le = input("Escolha sua Letra (X/O): ")
    if Le == "X" or Le == "O" or Le == "x" or Le == "o":
        if Le == "X" or Le == "x":
            return "X"
        else:
            return "O"
    else:
        return Letra()


def PrimeiroJogador():
    """
    Define quem sera o primeiro jogador a começar a partida
    
    retorna o simbolo do primeiro   jogador
    """
    Primeiro = random.choice(["X","O"])
    if Primeiro == "X" or Primeiro == "O":
        if Primeiro == "X":
            return "X"
        else:
            return "O"

def imprimeTabuleiro(L1):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    print(f" {L1[7]} | {L1[8]} | {L1[9]} ")
    print(f"---+---+---")
    print(f" {L1[4]} | {L1[5]} | {L1[6]} ")
    print(f"---+---+---")
    print(f" {L1[1]} | {L1[2]} | {L1[3]} ")


def Jogada(L1):
    """
    Funçao que recebe o tabuleiro e o simbolo do jogador, e
    permite o usuario fazer a jogada e retorna a posiçao sele
    cionada

    parametros
    L1 = lista com os valores de cada posiçao do tabuleiro
    """
    print()
    print("Pense Bem")
    print()
    Local = input("Escolha o local da sua jogada:")
    if Local == "1" or Local == "2" or Local == "3" or Local == "4" or Local == "5" or Local == "6" or Local == "7" or Local == "8" or Local == "9":
        Local = int(Local)
        if Local == 1 or Local == 2 or Local == 3:
            if L1[Local] == " ":
                return Local
            else:
                print("Jogada Invalida")
                return Jogada(L1)
        if Local == 4 or Local == 5 or Local == 6:
            if L1[Local] == " ":
                return Local
            else:
                print("Jogada Invalida")
                return Jogada(L1)
        if Local == 7 or Local == 8 or Local == 9:
            if L1[Local] == " ":
                return Local
            else:
                print("Jogada Invalida")
                return Jogada(L1)
    else:
        return Jogada(L1)

def Ganhador(Posicao,Le):
    """
    Funçao de auxilio do verificarJogo, verfica quem ganhou e imprime 
    na tela , e retona quem ganho como um valor 
    a = 1 , usuario ganhou
    a = 2 , computador ganhou
    """
    if Posicao == Le:
        print("Voce Ganhou")
        a = 1
    else:
        print("O computador Ganhou")
        a = 2
    return a

def verificaJogo(Letra,p0,p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das posições no tabuleiro a cada jogada
    e verifica se alguem ganhou, caso alguem ganhe ,ira imprimir o tabuleiro
    e retornara que o jogo acabou e quem ganhou 
    a = 1 , usuario ganhou
    a = 2 , computado ganhou
    """
    a = 0
    L1 = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9]
    if p1 == p2 and p1 == p3 and p1 != " ":
        print("Acabou")
        imprimeTabuleiro(L1[:])
        a = Ganhador(p1,Letra)
        return "Fim", a 
    elif p4 == p5 and p4 == p6 and p4 != " ":
        print("Acabou")
        imprimeTabuleiro(L1[:])
        a = Ganhador(p4,Letra)
        return "Fim", a 
    elif p7 == p8 and p7 == p9 and p7 != " ":
        print("Acabou")
        imprimeTabuleiro(L1[:])
        a = Ganhador(p7,Letra)
        return "Fim", a 
    elif p1 == p4 and p1 == p7 and p1 != " ":
        print("Acabou")
        imprimeTabuleiro(L1[:])
        a = Ganhador(p1,Letra)
        return "Fim", a 
    elif p2 == p5 and p2 == p8 and p2 != " ":
        print("Acabou")
        imprimeTabuleiro(L1[:])
        a = Ganhador(p2,Letra)
        return "Fim", a 
    elif p3 == p6 and p3 == p9 and p3 != " ":
        print("Acabou")
        imprimeTabuleiro(L1[:])
        a = Ganhador(p3,Letra)
        return "Fim", a 
    elif p1 == p5 and p1 == p9 and p1 != " ":
        print("Acabou")
        imprimeTabuleiro(L1[:])
        a = Ganhador(p1,Letra)
        return "Fim", a 
    elif p3 == p5 and p5 == p7 and p3 != " ":
        print("Acabou")
        imprimeTabuleiro(L1[:])
        a = Ganhador(p3,Letra)
        return "Fim", a 
    elif p1 != " " and p2 != " " and p3 != " " and p4 != " " and  p5 != " " and p6 != " " and p7 != " " and p8 != " " and p9 != " ":
        print("Acabou")
        imprimeTabuleiro(L1[:])
        print("Empate!")
        return "Fim", a 
    return "Segue", a

def FraseEfeito(L,Letra,Vez):
    """
    Funçao que imprime algumas frases aleatorias na vez do computador e do jogador
    """
    Turno = turno(L,n = 0,b = 0)
    if Letra != Vez and Turno > 1:
        a = ["Nem tento","Vamos la","Vai perder","Ta dificel ?","Ja joguei com melhores","Boa jogada","Pessima escolha","Classico",]
        print()
        print("Computador diz:")
        print(random.choice(a))
        print()

def Fim(PontoVc,PontoPc):
    """
    Funçao que permite o usuario jogar novamente, caso queira
    e que imprime o placar final

    """
    abc = input("Deseja Jogar Novamente(S/N): ")
    if abc == "S" or abc == "s" or abc == "N" or abc == "n":
        if abc == "S" or abc == "s":
            Le = Letra()
            Vez = PrimeiroJogador()
            return Game(Le,Vez," "," "," "," "," "," "," "," "," "," ",PontoVc,PontoPc)
        else:
            print("Placar:")
            print(f"Computador:{PontoPc}")
            print(f"Voce:{PontoVc}")
            print("Fim")
    else:
        return Fim(PontoVc,PontoPc)

def Game(Le,Vez,p0 = " ",p1 = " ", p2 = " ", p3 = " ", p4 = " ", p5= " ", p6 = " ", p7 = " ", p8 = " ", p9 = " ",pontoVoce = 0,pontocomputador = 0):
    """
    Funçao que controla o jogo da velha,como de quem e a vez,em que turno esta,
    chamando funçoes (turno,imprimeTabuleiro,verificaJogo,Jogada)

    parametros
    le = Tabuleiro
    Vez = quem ira jogar (Computador/Usuario)
    p0 = espaço vazio
    p1 ate p9 = elemento de cada posiçao no tabuleiro

    """

    L1 = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9]
    Turno = turno(L1[1:],n = 0,b = 0)
    q1, ponto = verificaJogo(Le,p0,p1, p2, p3, p4, p5, p6, p7, p8, p9)
    if q1 == "Segue":
        if Turno == 1:
            print("O computador começa") if Le != Vez else print("Voce começa")
        if Le == Vez:
            imprimeTabuleiro(L1[:])
        else:
            FraseEfeito(L1[1:],Le,Vez)
        if Vez == Le:
            if Vez == "X":
                Local = Jogada(L1[:])
                L1[Local] = Le
                return Game(Le,"O",L1[0],L1[1],L1[2],L1[3],L1[4],L1[5],L1[6],L1[7],L1[8],L1[9],pontoVoce,pontocomputador)
            else:
                Local = Jogada(L1[:])
                L1[Local] = Le
                return Game(Le,"X",L1[0],L1[1],L1[2],L1[3],L1[4],L1[5],L1[6],L1[7],L1[8],L1[9],pontoVoce,pontocomputador)
        else:
            if Le == "X":
                PC = "O"
                Local = jogadaComputador(L1[:],PC)
                L1[Local] = PC
                return Game(Le,"X",L1[0],L1[1],L1[2],L1[3],L1[4],L1[5],L1[6],L1[7],L1[8],L1[9],pontoVoce,pontocomputador)
            else:
                PC = "X"
                Local = jogadaComputador(L1[:],PC)
                L1[Local] = PC
                return Game(Le,"O",L1[0],L1[1],L1[2],L1[3],L1[4],L1[5],L1[6],L1[7],L1[8],L1[9],pontoVoce,pontocomputador)
    else:
        if ponto == 1:
            pontoVoce += 1
        if ponto == 2:
            pontocomputador += 1
        return Fim(pontoVoce,pontocomputador)


def main():
    limpaTela()
    #Você pode, se quiser, comentar os dois prints abaixo:
    print(getNome())
    print(getMatricula())
    Le = Letra()
    Vez = PrimeiroJogador()
    Game(Le,Vez)
    
## NÃO ALTERE O CÓDIGO ABAIXO ##X
if __name__ == "__main__":
    main()