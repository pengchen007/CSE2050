## This problem is from the book "Perplexing Puzzles and Trantalizing Teasers" by Martin Gardner
from itertools import permutations

class Queue:
    def __init__(self):
        self._head = 0
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        item = self._L[self._head]
        self._head += 1
        return item

    def __len__(self):
        return len(self._L) - self._head

    def isempty(self):
        return len(self) == 0

    
class AdjacencySetGraph:
    def __init__(self, V, E):
        self._V = set()
        self._nbrs = {}
        for v in V: self.addvertex(v)
        for u, v in E: self.addedge(u, v)

    def vertices(self):
        return iter(self.__V)

    def edges(self):
        for u in self._V:
            for v in self.nbrs(u):
                yield(u, v)

    def addvertex(self, v):
        self._V.add(v)
        self._nbrs[v] = set()

    def addedge(self, u, v):
        self._nbrs[u].add(v)

    def nbrs(self, v):
        return iter(self._nbrs[v])


    def bfs(self, v):
        tree = {}
        
        tovisit = Queue()
        tovisit.enqueue((None, v))
        while tovisit:
            a, b = tovisit.dequeue()
            if b not in tree:
                tree[b] = a
                for n in self.nbrs(b):
                    tovisit.enqueue((b, n))
        return tree


    def showresult(self, u, v):
        tree = self.bfs(u)
        if v not in tree:
            return
        result =[]
        result.append(v)
        count = 1
        c = tree[v]
        while c != u:
            result.append(c)
            c = tree[c]
            count += 1
            if count > 8: return
        result.append(u)
        result.reverse()
        return result
    
def isneighbor(v1, v2):
    a = v1.index(0)
    b = v2.index(0)
    count = 0
    for n in range(len(v1)):
        if v1[n] != v2[n]:
            count += 1
        if count > 2:
            return False
    if a - b == 0:
        return False
    if abs(a-b) < 3:
        return True
    return False
    

def createedges(V):

    E = set()
    for u in V:
        for v in V:
            if isneighbor(u, v):
                E.add((u, v))
    return E


def dime_and_penny():

    items = [1, 1, 0, 10, 10]
    V = set()
    for p in permutations(items):
        V.add(p)

    E = createedges(V)
    

    coinsgraph = AdjacencySetGraph(V, E)
    return coinsgraph.showresult((1, 1, 0, 10, 10), (10, 10, 0, 1, 1))

dime_and_penny()
    
result = dime_and_penny()
print("***********************")
for v in result:
    print(v)
