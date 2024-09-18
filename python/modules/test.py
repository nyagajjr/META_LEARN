def reverse_seq(n):
    if n < 1:
        return False
    else:
        for i in range(n,0,-1):
            print(i)
            
print(reverse_seq(5))        