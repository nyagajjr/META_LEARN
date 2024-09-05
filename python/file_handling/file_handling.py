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

with open('C:/Users/nyaga/OneDrive/Desktop/Good Reads/Software_Development/META/htmlcss/python/file_handling/created.txt', 'a') as file:
    file.writelines('\nHello there. I have been created')
    
    
import random    
with open('C:/Users/nyaga/OneDrive/Desktop/Good Reads/Software_Development/META/htmlcss/python/file_handling/dogs_names.txt', 'r') as file:
    data = file.read()
    new_data = data.split('\n')
    print(random.choice(new_data))
    
    
    
def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    
    ### WRITE SOLUTION HERE
    list = []
    with open(file_name, 'r') as file:
        data = file.readlines()
        for line in data:
            list.append(line.strip())
        return list
    
print(read_file_into_list('C:/Users/nyaga/OneDrive/Desktop/Good Reads/Software_Development/META/htmlcss/python/file_handling/created.txt'))


def write_first_line_to_file(file_contents):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE

    with open(file_contents, 'r') as file:
        data = file[0]
        return data
        
print(write_first_line_to_file('C:/Users/nyaga/OneDrive/Desktop/Good Reads/Software_Development/META/htmlcss/python/file_handling/created.txt'))
        
    
    