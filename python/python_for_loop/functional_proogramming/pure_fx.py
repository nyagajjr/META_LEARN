# Pure functions are functions that don't alter the data outside its scope. e.g

my_list = [1,2,3,4,5]

def pure_fx(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

print(pure_fx(my_list, 6)) # Not accessing the outside data from my_list
print(my_list) #Maintains the original data

