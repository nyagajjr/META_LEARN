data = [2, 4, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(len(data))

data1 = [x+3 for x in data]
print(data1)

new_list = [i**2 for i in data]
print(new_list)

fourx = [x for x in new_list if x%4 == 0 ]
print("Divisible by four", fourx)


# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)


#Dict comprehension
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

months_j = [x for x in months if x[0] == 'J']
print(months_j)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)

#This is a set comprehension
set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

#Generator comprehension
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")