# coffee = ['Cappucino','Espresso','Decaf','Latte', 'Machaitto','Americano']

# def reverse(str):
#     for i in str:
#         return i[::-1] #returns only one element because return stops the function
    
# print(reverse(['Cappucino','Espresso','Decaf','Latte', 'Machaitto','Americano']))

coffee = ['Cappucino','Espresso','Decaf','Latte', 'Machaitto','Americano']

def reverse(str):
    new_str = []
    for i in str:
        new_str.append(i[::-1])
    return new_str
    
print(reverse(['Cappucino','Espresso','Decaf','Latte', 'Machaitto','Americano']))