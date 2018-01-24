def puzzle(L,i,visited):        
    if i == len(L)-1: return True
##    if L[i] == 0: return False
    if i in visited: return False
    if L[i]+i <= len(L)-1:
        if i > L[i]:
            visited.add(i)
            return(puzzle(L,i+L[i],visited) or puzzle(L,i-L[i],visited))
        else:
            visited.add(i)
            return (puzzle(L,i+L[i],visited))
    if L[i]+i > len(L)-1:
        if i > L[i]:
            visited.add(i)
            return(puzzle(L,i-L[i],visited))
        else:
            return False

s = set()
print(puzzle([3,6,4,1,3,4,2,5,3,0], 0, s))
