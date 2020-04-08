class Stack:

    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1

    def pop(self):
        if not self.empty():
            self.stack.pop(self.len_stack -1)
            self.len_stack -= 1

    def top(self):
        if not self.empty():
            return self.    stack[-1]
        return None

    def empty(self):
        if self.len_stack == 0:
            return True
        return False

    def length(self):
        return self.len_stack

A = Stack()
m = 1

while(m!=0):

    print("\n1 - Mostrar Pilha \n2 - Adicionar \n3 - Remover \n4 - Imprimir\n")
    m = int(input("Digite a opção: "))
    if(m<0 or m>4):
        while(m<0 or m>4):
            print("Opção errada!")
            m = int(input("Digite sua opção:"))

    if(m==1):
       print(A.length())


    if(m==2):
       livro = int(input("\nDiga quantos livros a serem adicionados: "))
       for i in range(0, livro):
          livro = input("\nDigite o livro {}: ".format(i+1))
          A.push(livro)

    elif(m==3):
      A.pop()

    elif(m==4):
      print("O livro do topo é o",A.top())

      break











