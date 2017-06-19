from Jogadas import *


class Solucao:

    def __init__ (self):
        self.tabuleiro = [ [0, 0, 1, 1, 1, 0, 0],
                           [0, 0, 1, 1, 1, 0, 0],
                           [1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, ' ', 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1],
                           [0, 0, 1, 1, 1, 0, 0],
                           [0 ,0 ,1 ,1 ,1 ,0 ,0] ]

        self.matriz = self.tabuleiro
        self.pilha=Pilha()
        self.pilha_mov = Pilha_mov()
        self.empilha = jogadas()
        self.count_jogadas = 0
        self.count_desempilhadas=0



    def Empilha(self,Linha=0,Coluna=0):

        while self.empilha.tem_peca_para_mexer():
            #PROCURAR PEÇA DO COMEÇO DO TABULEIRO
            if Linha == 0 and Coluna == 0:
                Linha,Coluna = self.empilha.procurar_peca()
                if Linha == 8 and Coluna == 8:
                    break
            #CONTINUAR PROCURANDO PEÇA NO TABULEIRO
            else:
                Linha,Coluna = self.empilha.procurar_peca(Linha,Coluna)
                if Linha == 8 and Coluna == 8:
                    break
            #EMPILHA JOGADA
            self.pilha.push(Linha,Coluna)
            #PROCURA DIREÇÃO
            direcao = self.empilha.direcao(Linha,Coluna)
            #JOGADA
            self.empilha.fazer_jogada(Linha,Coluna,direcao)
            #PILHA DE MOVIMENTOS
            self.pilha_mov.push(direcao)
            Linha=0
            Coluna=0
            self.count_jogadas +=1
        self.pilha.pop()

    def Desempilha(self):

        posicao=[]
        posicao=self.pilha.topo_pilha()

        direcao=[]
        direcao=self.pilha_mov.topo_pilha_mov()

        if len(direcao) == 1:

            self.empilha.voltar_jogada(posicao,direcao[0])
            self.pilha_mov.pop()
            self.pilha.pop()
            self.pilha.aumentar_pilha()
            self.count_desempilhadas+=1
            return (posicao[0],posicao[1]+1)

        elif len(direcao) > 1:
            self.empilha.voltar_jogada(posicao,direcao[0])
            self.pilha_mov.pop_mov()
            self.empilha.fazer_jogada(posicao[0],posicao[1],direcao[0])
            self.pilha.aumentar_pilha()
            self.count_desempilhadas+=1
            return (0,0)

    def resolver(self):
        self.empilha.printar_tab()
        print("\n \t Resolvendo,aguarde...\n")
        self.Empilha()
        while self.empilha.jogo_acabou():


            Linha,Coluna = self.Desempilha()
            if self.pilha.tamanho() == 0:
                break
            self.Empilha(Linha,Coluna)

        if not self.empilha.jogo_acabou():
            self.empilha.printar_tab()
            print("\nJogadas: %d\n Desempilhadas: %d"%(self.count_jogadas,self.count_desempilhadas))
        else:
            self.empilha.printar_tab()
            print("\n Este tabuleiro nao tem solução")

teste = Solucao()

teste.resolver()
