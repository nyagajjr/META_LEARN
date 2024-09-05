# Sum of First N Natural Numbers

# Write a program to calculate the sum of the first N natural numbers using a for loop. For example, if N = 10, the output should be 55.


def sum_of_nums(n):
    summer = 0
    for i in range(1, n+1):
        summer += i
    print(summer)
        

sum_of_nums(10)        