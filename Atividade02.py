#Scrip de uma fila

class Queue:
    
    def __init__(self):
        self.queue = []
        self.len_queue = 0

    #PUSH É PARA ACRESCENTAR

    def push(self, e):
        self.queue.append(e)
        self.len_queue += 1

    #Listar fila

    def listar(self):
        for e in self.queue:
            print("\n"+e)

    #POP É PARA RETIRAR

    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1
    
    #EMPTY É PARA SABER SE A LISTA TÁ VAZIA OU NÃO (TRUE ou FALSE)
    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    #LENGTH É O TAMANHO DA LISTA

    def length(self):
        return self.len_queue

    #FRONT É O PRIMEIRO DA FILA.

    def front(self):
        if not self.empty():
            return self.queue[0]
        return None

#Desenvolva uma fila de carros(mostre a fila, insira carros, remova carros e imprima a lista de carros)

q = Queue()
x = 1

while(x!=0):

    print("\n[1] - Adicionar carros\n[2] - Remover o primeiro carro\n[3] - Ver lista de carros\n[4] - Ver quantidade de carros\n[0] - Sair\n")
    x = int(input("Digite sua opção: "))
    if(x<0 or x>4):
        while(x<0 or x>4):
            print("\nOpção inválida!!! \n")
            x = int(input("Digite sua opção: "))
            
    if(x==1):
        opc = int(input("\nQuantidade de carros que deseja adicionar: "))
        for i in range (0,opc):
            carro = input("\nDigite o {}º carro: ".format(i+1))
            q.push(carro)
    elif(x==2):
        q.pop()
    elif(x==3):
            q.listar()
    elif(x==4):
        print("\nA fila tem {} carro(s)".format(q.length()))
    else:
        print("\nSaindo .............................................\n")
        break        
