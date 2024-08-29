#reading a file
file = open('C:/Users/nyaga/OneDrive/Desktop/Good Reads/Software_Development/META/htmlcss/python/file_handling/test.txt', mode = 'r')

data = file.readline()

print(data)

file.close()

#reading file using with
with open('C:/Users/nyaga/OneDrive/Desktop/Good Reads/Software_Development/META/htmlcss/python/file_handling/test.txt', mode = 'r') as file:
    data = file.readline()
    print(data)
    

# #creating file

with open('C:/Users/nyaga/OneDrive/Desktop/Good Reads/Software_Development/META/htmlcss/python/file_handling/created.txt', 'w') as file:
    file.writelines('\nHello there. I have been created')
    