sample_dict = {1:'coffee', 2:'Tea', 3:'Juice'}
print(sample_dict[3])

del sample_dict[2]

print(sample_dict)

my_dict = {1: 'test', 'Name':'Oscilloscope'}

#Outputs only keys
for x in my_dict:
    print(x, " is a key")

#Outputs both key and values
for x, y in my_dict.items():
    print(str(x) + " : " + y)