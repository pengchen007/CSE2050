def indexMatch(list1):
    global listMedian
    left,right = 0,len(list1)        
    indexmedian = (left+right)//2
    while right - left > 1:       
        if list1[indexmedian] == indexmedian:
            listMedian.append(indexmedian)
            return indexmedian
        if list1[indexmedian] < indexmedian:
            listMedian.append(indexmedian)
            left = indexmedian
            indexmedian = (left+right)//2
        else:
            listMedian.append(indexmedian)
            right = indexmedian
            indexmedian = (left+right)//2
    if list1[0] == 0:
        return list1[0]
    return ("No Match Found!") # the function should return "No Match Found!" if there is no list1[i] = i 

listMedian = [] # this line must be kept for submission

## Code below are for testing purposes. Please delete or comment out the following code before submitting your code to Mimir.
list1 = [0, 2, 3, 4, 5, 10, 18, 45, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print("list1:", list1)
print("indexMatch:", indexMatch(list1))
print("listMedian:", listMedian)

