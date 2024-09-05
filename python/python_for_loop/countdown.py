# Count Down from 10 to 1

# Write a program to print numbers from 10 to 1 using a for loop.

def count_down(n):
    # n --> start value, -1 --> stop value, -1 --> step value, determines the decrement in each iteration
    for i in range(n, -1, -2):
        print(i)
        
count_down(12)