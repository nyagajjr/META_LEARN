# Using loop
# Input = 5    --output = 120

def factorial(n):
    counter = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            counter = counter * i
        return counter
    
print(factorial(5))

# using recursive function
def fact_rec(num):
    if num == 0 or num == 1:
        return 1
    return num * fact_rec(num - 1)

print(fact_rec(5))
            