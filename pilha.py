class Pilha:

    def __init__(self):
        self.pilha=[]
        self.pilha.append([])
    def vazia(self):
        return self.pilha[0] == []
    def tamanho(self):
        return len(self.pilha)-1
    def topo_pilha(self):
        return self.pilha[self.tamanho()]
    def push(self,y,x):
        self.pilha[self.tamanho()].append(y)
        self.pilha[self.tamanho()].append(x)
        self.pilha.append([])
    def pop(self):
        return self.pilha.pop()
    def aumentar_pilha(self):
        self.pilha.append([])
    def print_pilha(self):
        print(self.pilha)

class Pilha_mov:

    def __init__(self):
        self.pilha=[]
    def vazia(self):
        return self.pilha == []
    def tamanho(self):
        return len(self.pilha)-1
    def topo_pilha_mov(self):
        return self.pilha[self.tamanho()]
    def push(self,x):
        self.pilha.append(x)
    def pop(self):
        return self.pilha.pop()
    def pop_mov(self):
        return self.pilha[self.tamanho()].pop(0)
    def aumentar_pilha(self):
        self.pilha.append([])
    def print_pilha(self):
        print(self.pilha)
