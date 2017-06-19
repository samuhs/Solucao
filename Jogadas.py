from pilha import*

class jogadas:

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

    def procurar_peca(self,Linha=0,Coluna=0):
        for i in range(Linha,7):
            for j in range(Coluna,7):
                if self.movimento(i,j):
                    return (i,j)
            Coluna = 0
        else: return(8,8)

    def tem_peca_para_mexer(self,Linha=0,Coluna=0):

        for i in range(Linha,7):
            for j in range(Coluna,7):
                if self.movimento(i,j):
                    return True
        else: return False

    def jogo_acabou(self):
        b =0
        for i in range(len(self.matriz)):
            a = self.matriz[i]
            for j in range(len(a)):
                if a[j] == 1:
                    b+=1
        if b == 1:
            return False
        else:
            return True



    def movimento(self,Linha,Coluna):

        if self.matriz[Linha][Coluna] == 0 or self.matriz[Linha][Coluna]== ' ':
            return False

        down = Linha+2
        if down < 7:
            if self.matriz[down][Coluna] == ' ' and self.matriz[Linha+1][Coluna] == 1:
                return True

        up = Linha-2
        if up >= 0:
            if self.matriz[up][Coluna] == ' ' and self.matriz[Linha-1][Coluna] == 1:
                return True

        right = Coluna+2
        if right < 7:
            if self.matriz[Linha][right] == ' ' and self.matriz[Linha][Coluna+1] == 1:
                return True

        left = Coluna-2
        if left >= 0:
            if self.matriz[Linha][left] == ' ' and self.matriz[Linha][Coluna-1] == 1:
                return True

        else:
            return False

    def direcao(self,Linha,Coluna):

        direcao = []
        up = Linha-2
        if up >= 0:
            if self.matriz[up][Coluna] == ' ' and self.matriz[Linha-1][Coluna] == 1:
                direcao.append('w')

        right = Coluna+2
        if right < 7:
            if self.matriz[Linha][Coluna+2] == ' ' and self.matriz[Linha][Coluna+1] == 1:
                direcao.append('d')


        down = Linha+2
        if down < 7:
            if self.matriz[down][Coluna] == ' ' and self.matriz[Linha+1][Coluna] == 1:
                direcao.append('s')

        left = Coluna-2
        if left >= 0:
            if self.matriz[Linha][left] == ' ' and self.matriz[Linha][Coluna-1] == 1:
                direcao.append('a')

        return direcao

    def fazer_jogada(self,Linha,Coluna,direcao):

        letra = direcao[0]
        self.matriz[Linha][Coluna] = ' '
        if letra == 's':
            self.matriz[Linha+1][Coluna] = ' '
            self.matriz[Linha+2][Coluna] = 1
            return direcao

        elif letra == 'w':
            self.matriz[Linha-1][Coluna] = ' '
            self.matriz[Linha-2][Coluna] = 1
            return direcao

        elif letra == 'd':
            self.matriz[Linha][Coluna+1] = ' '
            self.matriz[Linha][Coluna+2] = 1
            return direcao

        elif letra == 'a':
            self.matriz[Linha][Coluna-1] = ' '
            self.matriz[Linha][Coluna-2] = 1
            return direcao

        else:
            print("**Movimento Invalido!**")

    def voltar_jogada(self,posicao,direcao):

        self.matriz[posicao[0]][posicao[1]] = 1
        if direcao == 's':
            self.matriz[posicao[0]+1][posicao[1]] = 1
            self.matriz[posicao[0]+2][posicao[1]] = ' '

        elif direcao == 'w':
            self.matriz[posicao[0]-1][posicao[1]] = 1
            self.matriz[posicao[0]-2][posicao[1]] = ' '

        elif direcao == 'd':
            self.matriz[posicao[0]][posicao[1]+1] = 1
            self.matriz[posicao[0]][posicao[1]+2] = ' '

        elif direcao == 'a':
            self.matriz[posicao[0]][posicao[1]-1] = 1
            self.matriz[posicao[0]][posicao[1]-2] = ' '

    def printar_tab(self):
        if self.matriz != self.tabuleiro:
            print('\n')
            for i in range(7):
                linha = self.matriz[i]
                for j in range(7):
                    print(linha[j],end = ' ')
                print('\t',i+1)
            print("\n")
            for i in range(7):
                print(i+1,end = ' ')
            print('\n Cima: w\t Baixo: s\t Direita: d\t Esquerda: a\n')
        else:
            print('\n')
            for i in range(7):
                linha = self.tabuleiro[i]
                for j in range(7):
                    print(linha[j],end = ' ')
                print('\t',i+1)
            print("\n")
            for i in range(7):
                print(i+1,end = ' ')
            print('\n Cima: w\t Baixo: s\t Direita: d\t Esquerda: a\n')
