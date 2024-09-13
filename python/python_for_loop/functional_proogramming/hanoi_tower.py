# The objective is to move n number of disks from one tower to another following a set of rules. These rules are as follows: 

# Only one disk can be moved at a time 

# Only the upper disk of any of the towers can be moved 

# Larger disks cannot be placed over smaller disks

# In the optimal scenario of solving the puzzle, the total moves will be 2^n – 1 where n is the number of disks that need to be moved.

# Now let's examine how you can write code for this in Python... USing Recusion

def hanoi(disks, start, aux, end):
    if disks == 1:
        print('Disks {} moves from tower {} to tower {}'.format(disks, start, end))
        
        return 

    hanoi(disks - 1, start, end, aux)
    print('Disks {} moves from tower {} to tower {}'.format(disks, start, end))
    
    
# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')