# Print Numbers from 1 to n
# Write a program to print all the numbers from 1 to 20 using a for loop.

def print_seq():
    num = input("Enter a number: ")
    n = int(num)

    for i in range(1, n+1):
        print(i)
        
print_seq()

