# def read_file(file_name):
#     with open(file_name) as file:
#         data = file.read()
#     print(data)
#     return data
#     raise NotImplementedError()

# # read_file('created.txt')

# def read_file_into_list(file_name):
#     list = []
#     with open(file_name) as file:
#         for item in file:
#             list.append(item)
#         return list
#         raise NotImplementedError()
    
# def write_first_line_to_file(file_contents, output_filename):   
#     first_line = file_contents.split('\n')[0]
#     with open(output_filename, 'w') as file:
#         file.write(first_line)
#         return output_filename
#         raise NotImplementedError()

# def read_even_numbered_lines(file_name):     
#     with open(file_name) as file:
#         file_content = file.readlines()
#         even_lines = file_content[1::2]
#     return even_lines
#     raise NotImplementedError()
    
def read_file_in_reverse(file_name): 
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    # Reverse the list of lines
    reversed_lines = [line.strip() for line in reversed(lines)]
    
    print(reversed_lines)  # Print the list
    return reversed_lines
    raise NotImplementedError()
read_file_in_reverse('created.txt')

        
    
        

