def reverse_str(str):
    counter = ''
    
    for i in range(len(str) -1, -1, -1):
        counter += str[i]
        
    return counter
        
    
    
print(reverse_str('okay'))
print(reverse_str('okay'))
