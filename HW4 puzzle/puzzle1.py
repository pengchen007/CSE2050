def puzzle(L,i,visited):        
    if i == len(L)-1:
        return True
    if (i < 0) or (i >= len(L)) or (i in visited):
        return False        

    visited.add(i)
    return (puzzle(L,i+L[i],visited) or puzzle(L, i-L[i], visited))

s = set()
print(puzzle([3,6,4,1,3,4,2,5,3,0], 0, s))
