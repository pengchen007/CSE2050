import random

class AdjacencySetGraph:
    def __init__(self, V, E):
        self._V = set()
        self._nbrs = {}
        for v in V: self.addvertex(v)
        for u, v in E: self.addedge(u, v)

    def vertices(self):
        return iter(self._V)

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

    def dfs(self, v):
        tree = {}
        tovisit = [(None, v)]
        while tovisit:
            a, b = tovisit.pop()
            if b not in tree:
                tree[b] = a
                for n in self.nbrs(b):
                    tovisit.append((b, n))
        return tree

    def randomdfs(self, v):
        tree = {}
        tovisit = [(None, v)]
##        random.shuffle(tovisit)
        while tovisit:
            a, b = tovisit.pop()
            if b not in tree:
                tree[b] = a
                nbrs = list(self._nbrs)
                random.shuffle(nbrs)
                for n in nbrs:
                    tovisit.append((b, n))
        return tree

        ## Add your code here
        ## copy code from dfs and make changes
        ## only very small changes needed
        ## you need to use random.shuffle method
        
    
def knightsmove():


    b2 = 'b2'
    c2 = 'c2'
    d2 = 'd2'
    b3 = 'b3'
    d3 = 'd3'
    b4 = 'b4'
    c4 = 'c4'
    d4 = 'd4'
    e5 = 'e5'
    f5 = 'f5'
    g5 = 'g5'
    e6 = 'e6'
    g6 = 'g6'
    e7 = 'e7'
    f7 = 'f7'
    g7 = 'g7'

    V = [b2 , c2, d2, b3, d3, b4, c4, d4, e5, f5, g5, e6, g6, e7, f7, g7]
    
    E = [(b2, c4), (b2, d3),\
            (c2, b4), (c2, d4), \
            (d2, b3), (d2, c4), \
            (b3, d2), (b3, d4), \
            (d3, b2), (d3, b4), (d3, e5), \
            (b4, c2), (b4, d3), \
            (c4, b2), (c4, d2), (c4, e5), \
            (d4, b3), (d4, c2), (d4, e6), (d4, f5), \
            (e5, c4), (e5, d3), (e5, f7), (e5, g6), \
            (f5, d4), (f5, e7), (f5, g7), \
            (g5, e6), (g5, f7), \
            (e6, d4), (e6, g5), (e6, g7), \
            (g6, e5), (g6, e7), \
            (e7, f5), (e7, g6), \
            (f7, e5), (f7, g5), \
            (g7, e6), (g7, f5)]

    chessgraph = AdjacencySetGraph(V, E)

    ## We are repeating this at most 10000000 times to search for solutions
    ## We start from all the possible positions for the knight
    
    for i in range(1000000):
        for v in V:
            tree = chessgraph.randomdfs(v)

            

            

            ## tree above is a depth-frist search tree.
            ## This tree is implemented as a dictionary. For each key (vertex), the
            ## value is its parent vertex.
            ## Now we need to check whether this tree is actually linear.
            ## If this tree is linear(a straight line) then we have a solution.
            ## If this is true, we need to make a new dictionary that is the inverse
            ## of this dictionary tree. That is, the key and value is switched for each
            ## item. Using this inversed dictionary, print out all the moves the knight
            ## takes.
            ## Finally, return this inversed dictionary as the return value of the
            ## method knightsmove.
            

            if len(set(tree.values())) == len(V):
                
                inv_tree = {v:k for k, v in tree.items()}
                L = []
                for i in inv_tree.values():
                    L.append(i)

                a = 0
                while a < len(L)-1:
                    print(L[a]+"->",end = '')
                    a += 1
                print(L[a])                

                return inv_tree
    return None


inv_tree = knightsmove()
##keys = set(inv_tree.keys())
##values = set(inv_tree.values())
##assert(len(keys) == 16)
##assert(len(values) == 16)
##assert(None in keys - values)
##assert(len(keys^values) == 2)


    
    





