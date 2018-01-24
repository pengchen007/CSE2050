class Tree:

    def __init__(self, L):
        iterator = iter(L)
        self.data = next(iterator)
        self.children = [Tree(c) for c in iterator]

    def printpreorder(self):
        print(self.data)
        for child in self.children:
            child.printpreorder()

    def printpostorder(self):
        for child in self.children:
            child.printpostorder()
        print(self.data)

    def computespace(self):
        for child in self.children:
            if self.data[1] == None:
                x = child.computespace()
            else:
                x = child.computespace() + self.data[1]
            self.data = (self.data[0], x)
        return (self.data[1])
                       

    def printbookcontent(self, Title = True):
        if Title:
            print("Book Title: ",(self.data[0]))
        else:
            print((self.data[0]) ," page: " ,(self.data[1]))
        for child in self.children:
            child.printbookcontent(Title = False)



                



### All the codes listed below are for testing purposes only. Please comment them out before submitting to Mimir.
Tbook = [('Make Money Fast!', 0), [('1. Motivations', 2), [('1.1 Greed', 5)], [('1.2 Avidity', 10)]], [('2. Methods', 15), [('2.1 Stock Fraud', 20)], [('2.2 Ponzi Scheme', 25)], [('2.3 Bank Robbery', 30)]], [('References', 40)]]
treeBook = Tree(Tbook)
print("Call preorderprint method:")
treeBook.printpostorder()
print("Call printbookcontent method:")
treeBook.printbookcontent()

Tbook = [('Make Money Ultra Fast!', -1), [('1. Motivations', 2), [('1.1 Ultra Greed', 5)], [('1.2 Ultra Avidity', 10)]], [('2. Methods', 15), [('2.1 Stock Fraud', 20)], [('2.2 Ponzi Scheme', 25)], [('2.3 Bank Robbery', 30)]], [('References', 40)]]
treeBook = Tree(Tbook)
print("Call preorderprint method:")
treeBook.printpreorder()
print("Call printbookcontent method:")
treeBook.printpostorder()

Tbook = [('Make Money Super Fast!', None), [('1. Motivations', 2), [('1.1 Super Greed', 5)], [('1.2 Super Avidity', 10)]], [('2. Super Methods', 15), [('2.1 Stock Fraud', 20)], [('2.2 Ponzi Scheme', 25)], [('2.3 Bank Robbery', 30)]], [('References', 40)]]
treeBook = Tree(Tbook)
print("Call preorderprint method:")
treeBook.printpreorder()
print("Call printbookcontent method:")
treeBook.printbookcontent()

Tfile = [('CSE2050/', None), [('HWs/', None), [('hw1.doc', 5)], [('hw2.doc', 15)]], [('LABs/', None), [('lab1.py', 7)], [('lab2.py', 10)], [('lab3.py', 10)]], [('ToDoList.txt', 20)]]
treeFile = Tree(Tfile)
print("Original File System Tree:")
treeFile.printpreorder()
print("\nCompute Space...\n")
treeFile.computespace()
print("File System Tree After Computing Space:")
treeFile.printpreorder()
