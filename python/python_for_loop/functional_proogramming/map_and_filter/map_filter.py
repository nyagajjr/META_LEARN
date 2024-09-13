# Map() function

menu = ['Espresso','Mocha','Latte','Cappuccino','Cortado','Americano']

# A function to find coffee that starts with 'C'
def find_coffee(coffee):
    if coffee[0] == 'C':
        return coffee
# We use map() 
# map_coffee = map(find_coffee,menu)
# print(map_coffee)
# for i in map_coffee:
#     print(i)
    
    
    
# Filter function

def fil_coffee(coffee):
    if coffee[0] == 'C':
        return coffee
# We use filter() 
filter_coffee = filter(fil_coffee,menu)
for i in filter_coffee:
    print(i)
