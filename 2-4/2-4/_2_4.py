def snakefill(n):
    eat,l  = 1,1
    while n**2 > l:
        l = l*2;
        eat+=1
    return eat - 2
        
print(snakefill(24))
