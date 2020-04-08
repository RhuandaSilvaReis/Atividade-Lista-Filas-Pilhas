class Node:

    def __init__(self, av):
        self.av = av
        self.next = None

    def getA(self):
        return self.av

    def setA(self, av):
        self.av = av

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self,av,index):
        if index >=0:
            node = Node(av)
        if self.empty():
            self.first = node
            self.last = node
        else:
            if index == 0:
                node.setNext(self.first)
                self.first = node
            elif index >= self.len_list:
                self.last.setNext(node)
                self.last = node
            else:

                prev_node = self.first
                curr_node = self.first.getNext()
                curr_index = 1
                while curr_node != None:
                    if curr_index == index:
                        Node.setNext(curr_node)
                        prev_node.setNext(node)
                    prev_node = curr_node
                    curr_node = curr_node.getNext()
                    curr_index +=1

                self.len_list+=1

    def pop(self, index):
        if not self.empty() and index >=0 and index < self.len_list:
            flag_remove = False
        if self.first.getNext() ==  None:
            self.first = None
            self.last = None
            flag_remove = True
        elif index == 0:
            self.first = self.first.getNext()
            flag_remove = True
        else:
            prev_node = self.first
            curr_node = self.first.getNext()
            curr_index = 1
            while curr_node != None:
                if index == curr_index:
                    prev_node.setNext(curr_node.getNext())
                    curr_node.setNext(None)
                    flag_remove = True
                    break
                prev_node = curr_node
                curr_node = curr_node.GetNext()
                curr_index += 1
        if flag_remove:
            self.len_list -= 1



    def empty(self):
      if self.first==None:
       return True
      return False

    def length(self):
     return self.len_list

    def show(self):

        curr_node = self.first
        
        while curr_node != None:
            print(curr_node.getA(), end='')
            curr_node = curr_node.getNext()
        print('')

L = LinkedList()
s = 1

while(s!=0):

    print("Escolha umas das opções para fazer a inserção, remoção ou imprimir a lista:")
    print("\n1 - Adicionar nome e idade. \n2 - Remover nome e idade. \n3 - Imprimir a lista.\n4 - Sair\n")
    s = int(input("Digite sua opção:"))
    if(s<0 or s>4):
        print("\nErro!\n")
        s = int(input("\nDigite a opção: \n "))

    if(s==1):

        Dados = input("\nInforme nome e idade separados: \n")
        L.push(Dados, 0)


    elif(s==2):
        L.pop(0)

    elif(s==3):
        print("\nDados adicionados:")

        L.show()

    else:
        print(".............Saindo.............")

        break










