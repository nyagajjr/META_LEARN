tup =(1,2,3, True, "str_")

print(type(tup))
# print(*tup)

empt = []
for i in tup:
    empt.append(i)
print(*empt, sep=", ")
    
    
# def blub():
#     a = list()
#     a.append(2.0)
#     print(a)

# blub()

